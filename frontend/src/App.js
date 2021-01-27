import React from 'react';
import Header from '../src/components/layout/Header';
import LandingPage from '../src/components/pages/LandingPage';
import Footer from '../src/components/layout/Footer';


function App() {
  return (
    <div className="App">
      <Header/>
      <LandingPage/>
      <Footer/>
    </div>
  );
}

export default App;
