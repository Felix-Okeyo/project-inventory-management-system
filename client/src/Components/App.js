
import React, { useEffect, useState } from 'react';
import NavBar from "./Navbar";
import { BrowserRouter as Router, Switch, Route, Redirect } from "react-router-dom";
import Home from "./Home";

import './Body.css';
import Products from "./Products";
import Outgoing from "./Outgoing";
import Supplier from "./Supplier";
import NewProduct from './NewProduct';
import LandingPage from './LandingPage';
import LoginForm from './Login';
import SignUpForm from './Signup';

function App() {
  const [products, setProducts] = useState([]);
  const [isLoggedIn, setIsLoggedIn] = useState(false); // Authentication state
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [email, setEmail] =useState('')
  const [first_name, setFirstName] = useState('')
  const [second_name, setSecondName]=useState('')
  const [access_token, setAccessToken] = useState(null);
  const [isRegistered, setIsRegistered] = useState(false);
  const headers = {
    'Authorization': `Bearer ${access_token}`,
    'Content-Type': 'application/json',
  }; 
  console.log(headers);
  useEffect(() => {
    fetch('https://inventory-ms-server-api.onrender.com/products',{  method: 'GET', 
    headers: headers,
  })
        .then((r) => r.json())
        .then((data) => {
          setProducts(data);
          console.log(data);
        });
    }
  , []);

  console.log(access_token);

  const addProduct = (newProduct, supplierId) => {
    console.log(supplierId);

    // Make a POST request to add the product to the specific supplier
    fetch(`https://inventory-ms-server-api.onrender.com/suppliers/${newProduct}`, {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${access_token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(supplierId), // Convert the newProduct object to JSON
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response if needed
        console.log(data);

        // Add the new Product to the local state
        setProducts([...products, data]);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  const onDeleteProduct = (productId) => {
    // Create a new array of products without the product with the given ID
    const updatedProducts = products.filter((product) => product.id !== productId);

    // Update the state with the new array of products
    setProducts(updatedProducts);
  };

  const onSearch = (type) => {
    if (type === "" || type === null) {
      // Display all the transactions
      fetch("https://inventory-ms-server-api.onrender.com/products",{  method: 'GET', 
      headers: headers,
    })
        .then((r) => r.json())
        .then((data) => {
          console.log("Fetched data:", data);
          setProducts(data);
        });
    } else {
      const filtered = products.filter((product) =>
        product.type.toLowerCase().includes(type.toLowerCase())
      );

      setProducts(filtered);
      console.log(filtered);
    }
  };
  const handleLogin = async (e) => {
    e.preventDefault();

    fetch('https://inventory-ms-server-api.onrender.com/login', {
  method: 'POST',
  headers: {
   
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    username: username,
    password: password,
  }),
})

  .then((response) => {
    if (response.status === 200) {
      response.json().then(data => {
        const accessToken = data.access_token; // Replace 'access_token' with the actual key
        setAccessToken(accessToken);
      });
      setIsLoggedIn(true);
    } else {
      // Handle login failure here, e.g., show an error message
      console.error('Login failed');
    }
  })
  .catch((error) => {
    // Handle any network request errors here
    console.error('Network error:', error);
  });

  };
  const handleSignUp= async (e) => {
    e.preventDefault();

    fetch('https://inventory-ms-server-api.onrender.com/register', {
  method: 'POST',
  headers: {
   
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    first_name:first_name,
    second_name:second_name,
    username: username,
    email: email,
    password: password,
  }),
})
.then((response) => {
  if (response.status === 201) {
    response.json().then(data => {
      const accessToken = data.access_token; // Replace 'access_token' with the actual key
      setAccessToken(accessToken);
    });
    setIsRegistered(true);
  } else {
    // Handle login failure here, e.g., show an error message
    console.error('Login failed');
  }
})
.catch((error) => {
  // Handle any network request errors here
  console.error('Network error:', error);
});

}

  return (
    <>
      <Router>
        <NavBar />
        <Switch>
          <Route exact path="/" ><LandingPage  /></Route>
            
          
          <Route path="/home" exact component={Home} />
          <Route path="/Products">
            {/* Pass the products data and addProduct function to the Products component */}
            <Route path="/Products">
  {isRegistered || isLoggedIn ? (
    <Products products={products} addProduct={addProduct} onDeleteProduct={onDeleteProduct} onSearch={onSearch} />
  ) : (
    <Redirect to="/" />
  )}
 </Route>

          </Route>
          <Route path="/Outgoing">
      {isRegistered || isLoggedIn ? (
        <Outgoing />
      ) : (
        <Redirect to="/" />
      )}
     </Route>
          
          <Route path="/Supplier">
      {isRegistered || isLoggedIn ? (
        <Supplier access_token={access_token} headers={headers} />
      ) : (
        <Redirect to="/" />
      )}
    </Route>
          <Route exact path="/login"><LoginForm isLoggedIn={isLoggedIn} handleLogin={handleLogin} username={username} password={password} setPassword={setPassword} setUsername={setUsername}/></Route>
          <Route exact path="/signup"><SignUpForm isRegistered={isRegistered} handleSignUp={handleSignUp} username={username} password={password} setPassword={setPassword} setUsername={setUsername} first_name={first_name} setFirstName={setFirstName} second_name={second_name} setSecondName={setSecondName} email={email} setEmail={setEmail}/></Route>
       
          
          <Route path="/new-product/:supplierId">
            {/* Pass the addProduct function to the NewProduct component */}
            <NewProduct addProduct={addProduct} />
          </Route>
        </Switch>
      </Router>
    </>
  );
}


export default App;
