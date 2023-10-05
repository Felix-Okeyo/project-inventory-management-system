import React, { useEffect, useState } from 'react';
import ProductList from './ProductList';
import './Body.css';

function Products({ products ,onDeleteProduct,onSearch}) {
  return (
    <>
      <h1>Product Inventory</h1>
      <ProductList products={products} onDeleteProduct={onDeleteProduct} onSearch={onSearch}/>
    </>
  );
}

export default Products;
