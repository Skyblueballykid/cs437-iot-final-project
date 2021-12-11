import React from 'react'
import ReactDOM from 'react-dom'
import './index.css'
import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom"
import { Typography, Box, Paper, Grid, Breadcrumbs } from '@mui/material';
import { Link } from "react-router-dom";

import App from './App'
import Audio from "./pages/audio";
import Item from "./pages/item";

ReactDOM.render(
  <React.StrictMode>
  <BrowserRouter>
  <Typography variant="h3">Team Thundercats Realtime Weather Detection Final Project</Typography> 
  <br/>
  <Typography variant="h6">UIUC CS 437: Internet of Things</Typography> 
      <br/>
      <br/>
      <div role="presentation">
      <Breadcrumbs aria-label="breadcrumb">
      <Link to="/">Home</Link>
      <Link to="/audio">Audio Recognition</Link>
      <Link to="/item">Item Recognition</Link>
      </Breadcrumbs>
    </div>
  <Routes>
      <Route path="/" element={<App />} />
      <Route path="audio" element={<Audio />} />
      <Route path="item" element={<Item />} />
    </Routes>
  </BrowserRouter>
  </React.StrictMode>,
  document.getElementById('root')
)
