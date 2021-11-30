import React, {useState, useEffect} from 'react'
import { styled } from '@mui/material/styles';
import { Typography, Box, Paper, Grid, Breadcrumbs, Link } from '@mui/material';
import Chart from "react-apexcharts";
import GoogleMapReact from 'google-map-react';
import { Sparklines, SparklinesLine } from 'react-sparklines';


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


var tempOptions = {
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
  labels: ["Temperature"]
};

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


var windSpeedOptions = {
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
  labels: ["Wind Speed"]
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
          <br/>
          <Item>
          Sensor Readings
          <br/>
          <Chart
              options={tempOptions}
              series={tempSeries}
              type="radialBar"
              width="170"
            />
            <br/>
        <Sparklines data={[5, 10, 5, 20]} limit={5} width={700} height={50} margin={1}>
          <SparklinesLine color="blue" />
        </Sparklines>
          <Chart
              options={humidityOptions}
              series={humiditySeries}
              type="radialBar"
              width="170"
            />
        <Sparklines data={[66, 32, 81, 19]} limit={5} width={700} height={50} margin={1}>
          <SparklinesLine color="blue" />
        </Sparklines>
           <Chart
              options={windSpeedOptions}
              series={windSpeedSeries}
              type="radialBar"
              width="170"
            />
          <Sparklines data={[6, 3, 12, 3]} limit={5} width={700} height={50} margin={1}>
          <SparklinesLine color="blue" />
        </Sparklines>
        </Item>
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
            <div style={{ height: '40vh', width: '100%' }}>
            <iframe src="http://68.225.115.149:8081/" width="100%" height="250" title="Weather Cam"></iframe>
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
