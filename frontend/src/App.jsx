import React from 'react'
import { styled } from '@mui/material/styles';
import { Typography, Box, Paper, Grid, Breadcrumbs, Link } from '@mui/material';
import Chart from "react-apexcharts";
import GoogleMapReact from 'google-map-react';
import { Sparklines, SparklinesLine } from 'react-sparklines';


const fetchData = () => {
  fetch(`https://telemetry-dropoff.s3.us-west-2.amazonaws.com/telemetry.json`)
    .then((response) => response.json())
    .then((json) => {
      console.log(json);
    })};

fetchData();

const REACT_APP_GOOGLE_MAPS_API_KEY = import.meta.env.VITE_APP_GOOGLE_MAPS_API_KEY
const mapProps = {
  center: {
    lat:  32.55705117,
    lng: -83.65685342
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

var tempSeries = [67];

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

var humiditySeries = [55];

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

var windSpeedSeries = [21];

function App() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <Typography variant="h3">Team Thundercats Realtime Weather Detection Final Project</Typography> 
      <br/>
      <br/>
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
            center={mapProps.center}
            defaultZoom={mapProps.zoom}
        ></GoogleMapReact></div>
          </Item>
        </Grid>
        <br/>
        <Grid item xs>
        <Item>Realtime Weather Camera
            <br/>
            <div style={{ height: '40vh', width: '100%' }}>
            <img src='./weather-placeholder.png'></img>
            </div>
          </Item>
        </Grid>
        </Grid>
      </Grid>
    </Box>
  );
}

export default App
