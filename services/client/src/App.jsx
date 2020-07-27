import React, { Component } from 'react';
import { Route, Switch } from 'react-router-dom'
import JConsole from './components/JConsole'
import './App.css';
import 'bootstrap/dist/css/bootstrap.min.css';

class App extends Component {

  render() {
    return (
      <div>
        <h1 id="title">J Interpreter</h1>
        <Switch>
          <Route exact path = '/' render={() => (
            <div>
              <JConsole/>
            </div>
          )}/>
        </Switch>
      </div>
    )
  }

}

export default App;
