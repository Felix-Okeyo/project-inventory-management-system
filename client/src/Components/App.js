
import React, { useEffect, useState } from 'react';
import NavBar from "./Navbar";
import { BrowserRouter as Router , Switch , Route } from "react-router-dom";
import Home from "./Home";
import Incoming from "./Incoming";
import './Body.css';
import Products from "./Products";
import Outgoing from "./Outgoing";
import Supplier from "./Supplier";
import NewProduct from './NewProduct';
// App.js
function App() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    fetch('http://127.0.0.1:5555/products')
      .then((r) => r.json())
      .then((data) => {
        setProducts(data);
        console.log(data);
      });
  }, []);

  const addProduct = (newProduct, supplierId) => {
    console.log(supplierId);
  
    // Make a POST request to add the product to the specific supplier
    fetch(`http://127.0.0.1:5555/suppliers/${newProduct}`, {
      method: 'POST',
      headers: {
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
      //display all the transactions
      fetch("https://api.npoint.io/e5115d936f381a580b81/products")
    .then((r) => r.json())
    .then((data) => {
      console.log("Fetched data:", data)
    
      setProducts(data)

     });
    } 
    else {
     
      const filtered = products.filter((product) =>
        product.type.toLowerCase().includes(type.toLowerCase())
      );
     
      setProducts(filtered);
      console.log(filtered)
    }
   
 
};


  return (
    <>
      <Router>
        <NavBar />
        <Switch>
          <Route path="/" exact component={Home} />
          <Route path="/Products">
            {/* Pass the products data and addProduct function to the Products component */}
            <Products products={products} addProduct={addProduct} onDeleteProduct={onDeleteProduct}  onSearch={onSearch}/>
          </Route>
          <Route path="/Incoming" component={Incoming} />
          <Route path="/Outgoing" component={Outgoing} />
          <Route path="/Supplier" component={Supplier} />
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