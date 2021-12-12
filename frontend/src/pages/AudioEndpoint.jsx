import React, { useState, useEffect } from 'react';


function flaskEndpoint() {
  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/test').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
    <div className="flaskEndpoint">
      <header className="flaskEndpoint">

        ... no changes in this part ...

        <p>The current time is {currentTime}.</p>
      </header>
    </div>
  );
}

export default flaskEndpoint;