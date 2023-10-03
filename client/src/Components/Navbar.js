import React, { useState } from "react";
import { Link } from "react-router-dom";



function NavBar() {
  const [isLoginFormOpen, setLoginFormOpen] = useState(false);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const toggleLoginForm = () => {
    setLoginFormOpen((prev) => !prev);
  };

  const handleLogin = () => {
    // Implement your login logic here
    console.log("Username:", username);
    console.log("Password:", password);
    // Reset form after login
    setUsername("");
    setPassword("");
    // Close the login form after successful login (You can handle actual authentication here)
    setLoginFormOpen(false);
  };

  return (
    <header className="Navbar">
      
      <div className="List">
        <ul className="list">
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/Products">Products</Link>
          </li>
          <li>
            <Link to="/Incoming">Incoming</Link>
          </li>
          <li>
            <Link to="/Outgoing">Outgoing</Link>
          </li>
          <li>
            <Link to="/Supplier">Supplier</Link>
          </li>
         
        </ul>
      </div>
      <svg
        xmlns="http://www.w3.org/2000/svg"
        classsName="cart"
        width="25"
        height="25"
        fill="currentColor"
        className="bi bi-cart3"
        viewBox="0 0 16 16"
        style={{ marginTop: "-120px", marginLeft: "1120px", color: "white" }}
      >
        {/* Your SVG path here */}
      </svg>
      <button
        type="button"
        className="btn btn-dark"
        onClick={toggleLoginForm}
        style={{
          color: "white",
          marginTop: "-65px",
          float: "right",
          marginRight: "65px",
          borderRadius: "100px",
        }}
      >
        {isLoginFormOpen ? "Close" : "Sign in"}
      </button>

      {isLoginFormOpen && (
        <div className="loginForm">
          <h2>Login Form</h2>
          <input
            type="text"
            placeholder="Username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
          />
          <input
            type="password"
            placeholder="Password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
          />
          <button onClick={handleLogin}>Login</button>
        </div>
      )}
    </header>
  );
}

export default NavBar;
