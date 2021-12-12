import React, { Component } from 'react';
import AudioAnalyser from './AudioAnalyser';
import AudioEndpoint from './AudioEndpoint';

class Audio extends Component {
  constructor(props) {
    super(props);
    this.state = {
      audio: null,
      record: false,
    };
    this.toggleMicrophone = this.toggleMicrophone.bind(this);
  }

  async getMicrophone() {
    const audio = await navigator.mediaDevices.getUserMedia({
      audio: true,
      video: false
    });
    this.setState({ audio });
  }

  stopMicrophone() {
    this.state.audio.getTracks().forEach(track => track.stop());
    this.setState({ audio: null });
  }

  toggleMicrophone() {
    if (this.state.audio) {
      this.stopMicrophone();
    } else {
      this.getMicrophone();
    }
  }

  startRecording = () => {
    this.setState({
      record: true
    });
  }

  stopRecording = () => {
    this.setState({
      record: false
    });
  }

  onData(recordedBlob) {
    console.log('chunk of real-time data is: ', recordedBlob);
  }

  onStop(recordedBlob) {
    console.log('recordedBlob is: ', recordedBlob);
  }

  render() {
    return (
      <div className="App">
        <div className="controls">
          <button onClick={this.toggleMicrophone}>
            {this.state.audio ? 'Stop microphone' : 'Get microphone input'}
          </button>
        </div>
        {this.state.audio ? <AudioAnalyser audio={this.state.audio} /> : ''}
        <div>
          <AudioEndpoint></AudioEndpoint>
        </div>
      </div>
    );
  }
}

export default Audio;
