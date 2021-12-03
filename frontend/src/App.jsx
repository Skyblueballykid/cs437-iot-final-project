import React, {useState, useEffect} from 'react'
import { styled } from '@mui/material/styles';
import { Typography, Box, Paper, Grid, Breadcrumbs, Link } from '@mui/material';
import Chart from "react-apexcharts";
import GoogleMapReact from 'google-map-react';
import { Sparklines, SparklinesLine } from 'react-sparklines';
import { Donut, White } from 'react-dial-knob';

const REACT_APP_GOOGLE_MAPS_API_KEY = import.meta.env.VITE_APP_GOOGLE_MAPS_API_KEY
const mapProps = {
  center: {
    lat:  40.116421,
    lng: -88.243385
  },
  zoom: 10
};

const Item = styled(Paper)(({ theme }) => ({
  ...theme.typography.body2,
  padding: theme.spacing(1),
  textAlign: 'center',
  color: theme.palette.text.secondary,
}));


var humidityOptions = {
  chart: {
    height: 80,
    type: "radialBar"
  },
  
  series: [67],
  
  plotOptions: {
    radialBar: {
      hollow: {
        margin: 15,
        size: "70%"
      },
     
      dataLabels: {
        showOn: "always",
        name: {
          offsetY: -10,
          show: true,
          color: "#888",
          fontSize: "13px"
        },
        value: {
          color: "#111",
          fontSize: "30px",
          show: true
        }
      }
    }
  },

  stroke: {
    lineCap: "round",
  },
  labels: ["Humidity"]
};


function App() {

  const [data, setData] = useState([]);
  const [tempSeries, setTempSeries] = useState([]);
  const [humiditySeries, setHumiditySeries] = useState([]);
  const [windSpeedSeries, setWindSpeedSeries] = useState([]);
  const [timestamp, setTimeStamp] = useState('');
  const [lat, setLat] = useState('');
  const [long, setLong] = useState('');
  const [toggle, setToggle] = useState(false);
  const [mapState, setMapState] = useState({
    center: {
      lat:  '',
      lng: ''
    },
    zoom: 10
  });

  useEffect(() => {
    const fetchData = async () => {
      const response = await fetch(`https://telemetry-dropoff.s3.us-west-2.amazonaws.com/telemetry.json`);
      const res = await response.json();
      setData(res);
      setTempSeries(res.map(item => item.temperature_fahrenheit));
      setHumiditySeries(res.map(item => item.humidity));
      setWindSpeedSeries(res.map(item => item.wind_mph));
      setTimeStamp(res[0].timestamp);
      setLat(res[0].gps_latitude);
      setLong(res[0].gps_longitude);
      setMapState({    
        center: {
        lat:  res[0].gps_latitude,
        lng: res[0].gps_longitude
      },
      zoom: 10
    })
    setToggle(true);
    };
    fetchData();
  }, []);

  return (
    <>
    {console.log(data)}
    <Box sx={{ flexGrow: 1 }}>
      <Typography variant="h3">Team Thundercats Realtime Weather Detection Final Project</Typography> 
      <br/>
      <br/>
      <div role="presentation">
      <Breadcrumbs aria-label="breadcrumb">
        <Link underline="hover" color="inherit" href="/">
          Home
        </Link>
        <Link
          underline="hover"
          color="inherit"
          href="/"
        >
          Audio Recognition
        </Link>
        <Link
          underline="hover"
          color="inherit"
          href="/"
        >
          Item Recognition
        </Link>
      </Breadcrumbs>
    </div>
    <br/>
      {timestamp ? <p>Date and time: {timestamp}</p> : null}
      <Grid 
      container
      spacing={1}>
        <br/>
        <Grid 
        item
        direction="column"
        justifyContent="center"
        alignItems="center" 
        xs={6}>
          <Item>
          <div style={{ height: '75vh', width: '100%' }}>
          <br/>
          Sensor Readings
          <br/>
            <White
            style={{position: "absolute", top: "40%", left: "25%", transform: "translate(-50%, -50%)"}}
            diameter={100}
            min={0}
            max={120}
            step={1}
            value={tempSeries}
            theme={{
                activeNotchColor: 'blue',
                defaultNotchColor: 'floralwhite'
            }}
            ariaLabelledBy={'temp'}
        >
        <label id={'temp'}>Temperature &#176; F</label>
    </White>
            <br/>
        {/* <Sparklines data={[5, 10, 5, 20]} limit={5} width={700} height={50} margin={1}>
          <SparklinesLine color="blue" />
        </Sparklines> */}
        <Chart
          style={{position: "absolute", top: "60%", left: "25%", transform: "translate(-50%, -50%)"}}
            options={humidityOptions}
            series={humiditySeries}
            type="radialBar"
            width="180"
          />
        {/* <Sparklines data={[66, 32, 81, 19]} limit={5} width={700} height={50} margin={1}>
          <SparklinesLine color="blue" />
        </Sparklines> */}
        <White
        style={{position: "absolute", top: "80%", left: "25%", transform: "translate(-50%, -50%)"}}
        diameter={100}
        min={0}
        max={100}
        step={1}
        value={windSpeedSeries}
        theme={{
          activeNotchColor: 'blue',
          defaultNotchColor: 'floralwhite'
      }}
        ariaLabelledBy={'wind'}
    >
        <label id={'wind'}>Wind Speed (MPH)</label>
    </White>
    </div>
    </Item>
          {/* <Sparklines data={[6, 3, 12, 3]} limit={5} width={700} height={50} margin={1}>
          <SparklinesLine color="blue" />
        </Sparklines> */}
        </Grid>
        <Grid 
        item
        direction="column"
        justifyContent="center"
        alignItems="center" 
        xs={6}>
        <Grid item xs={6}>
        <Item>Map
          <div style={{ height: '25vh', width: '100%' }}>
          <GoogleMapReact
            bootstrapURLKeys={{ key: REACT_APP_GOOGLE_MAPS_API_KEY }}
            center={toggle ? mapState.center : mapProps.center}
            defaultZoom={mapProps.zoom}
        ></GoogleMapReact></div>
          {lat && long ? <p>Latitude: {lat}, &nbsp; Longitude: {long}</p> : null}
          </Item>
        </Grid>
        <br/>
        <Grid item xs>
        <Item>Realtime Weather Camera
            <br/>
            <div style={{ height: '33vh', width: '100%' }}>
            <iframe src="https://68.225.115.149:8443/" width="100%" height="220" title="Weather Cam"></iframe>
            </div>
          </Item>
        </Grid>
        </Grid>
      </Grid>
    </Box>
    </>
  );
}

export default App
