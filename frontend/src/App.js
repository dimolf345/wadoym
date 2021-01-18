import React, { Component } from 'react';
import Header from '../src/components/layout/Header';

class App extends Component {
  constructor() {
    super();
  }
  render() {
    return (
      <div>
        <Header/>
        <h1>Welcome back</h1>
      </div>
    );
  }
}

export default App;
