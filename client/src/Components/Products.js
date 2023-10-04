import React ,{ useEffect, useState } from 'react'
import ProductList from './ProductList';
import './Body.css';

 function Products() {
    const[products ,setProducts]=useState([])
    useEffect(() => {
      fetch(' http://127.0.0.1:5555/products')
        .then((r) => r.json())
        .then((data) => {setProducts(data)
        console.log(data)});
    }, []);
  return < >
  <h1>Product Inventory</h1>
  <ProductList products={products}/>
  </>;
}
export default Products;