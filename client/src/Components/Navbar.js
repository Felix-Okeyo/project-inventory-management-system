import React from "react";
import { Link } from "react-router-dom";
import './Navbar.css';



function NavBar() {
  //const [isLoginFormOpen, setLoginFormOpen] = useState(false);
  //const [username, setUsername] = useState("");
  //const [password, setPassword] = useState("");

  // const toggleLoginForm = () => {
  //   setLoginFormOpen((prev) => !prev);
  // };

  // const handleLogin = () => {
  //   // Implement your login logic here
  //   console.log("Username:", username);
  //   console.log("Password:", password);
  //   // Reset form after login
  //   setUsername("");
  //   setPassword("");
  //   // Close the login form after successful login (You can handle actual authentication here)
  //   setLoginFormOpen(false);
  // };

  return (
    <header className="navbar">
      
      <div className="List">
        <ul className="list">
          <li>
            <Link to="/" className='nav-links'>Home</Link>
          </li>
          <li>
            <Link to="/Products" className='nav-links'>Products</Link>
          </li>
          <li>
            <Link to="/Incoming" className='nav-links'>Incoming</Link>
          </li>
          <li>
            <Link to="/Outgoing" className='nav-links'>Outgoing</Link>
          </li>
          <li>
            <Link to="/Supplier" className='nav-links'>Supplier</Link>
          </li>
         
        </ul>
      </div>
{/*     
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
      )} */}
    </header>
  );
}

export default NavBar;
