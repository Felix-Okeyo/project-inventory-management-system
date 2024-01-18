import React, { useState } from "react";
import { Link } from "react-router-dom";
import "./Navbar.css";
import "./Form.css";
// Import your LoginForm and SignUpForm components


function NavBar() {
  

 

  return (
    <header className="navbar">
      <div className="List">
        <ul className="list">
          <li>
            <Link to="/home" className="nav-links">
              Home
            </Link>
          </li>
          <li>
            <Link to="/Products" className="nav-links">
              Products
            </Link>
          </li>

          <li>
            <Link to="/Outgoing" className="nav-links">
              Shipping
            </Link>
          </li>
          <li>
            <Link to="/Supplier" className="nav-links">
              Supplier
            </Link>
          </li>
        </ul>
      </div>

      
     
      
    </header>
  );
}

export default NavBar;
