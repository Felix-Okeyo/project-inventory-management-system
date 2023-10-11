import React from 'react';
import { Redirect } from 'react-router-dom';
import './Login.css'
import starsVideo from "../stars.mp4"; 

function LoginForm({ isLoggedIn, handleLogin, username, password, setUsername, setPassword }) {
  if (isLoggedIn) {
    return <Redirect to="/home" />;
  }

  const onUsernameChange = (e) => {
    setUsername(e.target.value);
  };

  const onPasswordChange = (e) => {
    setPassword(e.target.value);
  };

  return (
    <>
    <video autoPlay muted loop id="myVideo" >
        <source src={starsVideo} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
    
    <div className="login-form">
      
      <h1>Login</h1>
      <form onSubmit={handleLogin}>
        <div className="form-group">
          <label htmlFor="username">Username</label>
          <input
            type="text"
            id="username"
            placeholder="Enter your username"
            value={username}
            onChange={onUsernameChange}
          />
        </div>

        <div className="form-group">
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            placeholder="Enter your password"
            value={password}
            onChange={onPasswordChange}
          />
        </div>

        <button type="submit">Login</button>
      </form>
    </div>
    </>
  );
}

export default LoginForm;
