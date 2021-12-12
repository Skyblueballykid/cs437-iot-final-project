import React, { useState, useEffect } from 'react';


function flaskEndpoint() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('http://127.0.0.1:5000/test',{headers : { 
      'Content-Type': 'application/json',
      'Accept': 'application/json'
     }}).then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
    <div>
      <header>

        ... no changes in this part ...

        <p>The current time is {currentTime}.</p>
      </header>
    </div>
  );
}

export default flaskEndpoint;