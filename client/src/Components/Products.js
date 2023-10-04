import React ,{ useEffect, useState } from 'react'
import ProductList from './ProductList';
import './Body.css';
import NewProduct from './NewProduct';

 function Products() {
    const[products ,setProducts]=useState([])
    const [showNewProduct, setShowNewProduct] = useState(false);
    useEffect(() => {
      fetch(' http://127.0.0.1:5555/products')
        .then((r) => r.json())
        .then((data) => {setProducts(data)
        console.log(data)});
    }, []);
    const addProduct = (newProduct) => {
      setProducts([...products, newProduct]);
    };
  return < >
  <h1>Product Inventory</h1>
  {/* Button to toggle the NewProduct component */}
  <button onClick={() => setShowNewProduct(!showNewProduct)} className='hide'>
        {showNewProduct ? 'Hide form' : 'Add New Product'}
      </button>
      
      {/* Conditional rendering of the NewProduct component */}
      {showNewProduct && <NewProduct addProduct={addProduct} />}
  <ProductList products={products}/>
  </>;
}
export default Products;