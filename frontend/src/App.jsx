import React from 'react'
import { styled } from '@mui/material/styles';
import { Typography, Box, Paper, Grid, Breadcrumbs, Link } from '@mui/material';
import Chart from "react-apexcharts";

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
  labels: ["Progress"]
};

var tempSeries = [67];

function App() {
  return (
    <Box sx={{ flexGrow: 1 }}>
      <Typography variant="h3">Team Thundercats Realtime Weather Detection Final Project</Typography> 
      <br/>
      <br/>
      <Grid container spacing={2}>
        <Grid item xs={6}>
          <Item>Sensor Readings
          <Chart
              options={tempOptions}
              series={tempSeries}
              type="radialBar"
              width="200"
            />
          <Chart
              options={tempOptions}
              series={tempSeries}
              type="radialBar"
              width="200"
            />
           <Chart
              options={tempOptions}
              series={tempSeries}
              type="radialBar"
              width="200"
            />
            </Item>
        </Grid>
        <Grid item xs={6}>
          <Item>Realtime Weather Camera</Item>
        </Grid>
        <Grid item xs={12}>
          <Item>Map</Item>
        </Grid>
      </Grid>
    </Box>
  );
}

export default App
