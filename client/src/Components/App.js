
import React from "react";
import NavBar from "./Navbar";
import { BrowserRouter as Router , Switch , Route } from "react-router-dom";
import Home from "./Home";
import Incoming from "./Incoming";

import Products from "./Products";
import Outgoing from "./Outgoing";
import Supplier from "./Supplier";
function App() {
  return (
    <>
    <Router>
      <NavBar/>
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/Products"  component={Products} />
        <Route path="/Incoming"  component={Incoming} />
        <Route path="/Outgoing"  component={Outgoing} />
        <Route path="/Supplier"  component={Supplier} />
      </Switch>
    </Router>
    </>
  );
}

export default App;


