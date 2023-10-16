// LandingPage.js
import React from 'react';
import { Link } from 'react-router-dom';
import starsVideo from "../stars.mp4"; 
import './Landinpage.css'
function LandingPage() {
  const buttonStyle = {
    display: 'block',
    margin: '30px auto', // Add margin to center buttons and separate them
    width: '700px', // Reduce button width
    textAlign: 'center',
    backgroundColor:'white',
    color:'black'

  };
  const containerStyle = {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    minHeight: '100vh', // Make the container fill the viewport height
  };

  return (
    <div>
      
      <video autoPlay muted loop id="myVideo" >
        <source src={starsVideo} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
      <div className='text-center' style={containerStyle}>
      <h1 style={{color:'white'}}>Welcome to JFX Inventory</h1>
      <Link to="/login">
        <button style={buttonStyle}>Login</button>
      </Link>
      <Link to="/signup">
        <button style={buttonStyle}>Sign Up</button>
      </Link>
      </div>
    </div>
  );
}

export default LandingPage;


