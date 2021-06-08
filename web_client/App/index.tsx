import React from 'react';
import ReactDOM from 'react-dom';
import { 
  Route, 
  BrowserRouter as Router,
  Switch
} from 'react-router-dom';

import 'bootstrap/dist/css/bootstrap.css';

const style = require('./index.css');

const App = () => {

  return(
    <div>
      <h1>Hello World</h1> 
    </div>
  );
}

ReactDOM.render(
    <App />,
  document.getElementById('app')
);
