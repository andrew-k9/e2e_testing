import React, { useState } from 'react';
import ReactDOM from 'react-dom';
import Button from 'react-bootstrap/Button';

import 'bootstrap/dist/css/bootstrap.css';

const style = require('./index.css');

const App = () => {

  const [saying, setSaying] = useState("hey");
  const handleClick = (event: any) => setSaying(saying + "y");

  return(
    <div id="app-main">
      <h1 id="header">Hello Selenium</h1> 
      <div id="-container">
        <h3 id="saying">{saying}</h3>
        <Button
          id="button"
          onClick={handleClick}
        >
          {'Add a y'}
        </Button>
      </div>
    </div>
  );
}

ReactDOM.render(
    <App />,
  document.getElementById('app')
);
