import React ,{ useEffect, useState } from 'react'
import ProductList from './ProductList';
import './Body.css';

 function Products() {
    const[areas ,setAreas]=useState([])
    useEffect(() => {
      fetch(' https://api.npoint.io/02ad3566d5665e942f97/areas')
        .then((r) => r.json())
        .then((data) => {setAreas(data)
        console.log(data)});
    }, []);
  return < >
  <h1>Product Inventory</h1>
  <ProductList areas={areas}/>
  </>;
}
export default Products;