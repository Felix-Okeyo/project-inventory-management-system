
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

  const addProduct = (newProduct) => {
    console.log(newProduct);
    // Add the new product to the products state
    setProducts([...products, newProduct]);
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
      fetch("http://127.0.0.1:5555/products")
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