import React, { useState, useEffect } from 'react';


function flaskEndpoint() {
  const [currentSound, setCurrentSound] = useState(0);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/sound',{headers : { 
      'Content-Type': 'application/json',
      'Accept': 'application/json'
     }}).then(res => res.json()).then(data => {
      setCurrentSound(data.sound);
    });
  }, []);

  return (
        <p>Sound detected: {currentSound}.</p>
  );
}

export default flaskEndpoint;