// SignUpForm.js
// SignUpForm.js
import React from 'react';
import { Redirect } from 'react-router-dom';
import './Signup.css'
import starsVideo from "../stars.mp4"; 

function SignUpForm({ isRegistered, handleSignUp, username, password, setUsername, setPassword, first_name, second_name, email, setFirstName, setSecondName, setEmail }) {
  if (isRegistered) {
    return <Redirect to="/home" />;
  }

  return (
    <>
    <video autoPlay muted loop id="myVideo" >
        <source src={starsVideo} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    <div className="signup-form">
      <h1>Sign Up</h1>
      <form onSubmit={handleSignUp}>
        <div className="form-group">
          <label htmlFor="first_name">First Name</label>
          <input
            type="text"
            id="first_name"
            placeholder="Enter your first name"
            value={first_name}
            onChange={(e) => setFirstName(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label htmlFor="second_name">Second Name</label>
          <input
            type="text"
            id="second_name"
            placeholder="Enter your second name"
            value={second_name}
            onChange={(e) => setSecondName(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label htmlFor="email">Email</label>
          <input
            type="text"
            id="email"
            placeholder="Enter your email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label htmlFor="username">Username</label>
          <input
            type="text"
            id="username"
            placeholder="Choose a username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
        </div>

        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            placeholder="Enter your password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
        </div>

        <button type="submit">Sign Up</button>
      </form>
    </div>
    </>
  );
}

export default SignUpForm;
