import React, { useState } from 'react';
import Searchbar from './Searchbar';

const ProductList = ({ products, onDeleteProduct ,onSearch}) => {
  


  // Function to delete a product by ID
  const handleDeleteProduct = (productId) => {
    onDeleteProduct(productId);
  };
  //Filter bots based on the entered class
  
  return (
    
    <div className="Products">
      <Searchbar onSearch={onSearch}/>

      <div className="cardis">
        {products.length === 0 ? (
          <div className="col-12">
            <h2 style={{ color: 'white' }}>No Matches Found</h2>
          </div>
        ) : (
          products.map((product) => (
            <div key={product.id} className="cards__item__link">
              <figure className="cards__item__pic-wrap">
                <img className="cards__item__img" src={product.image} alt="Your product" />
              </figure>
              <div className="cards__item__info">
                <h5 className="cards__item__text">{product.product_name}</h5>

                <p className="cards__item__text">{product.type}</p>
                <p className="cards__item__text">quantity: {product.quantity}</p>
                <p className="cards__item__text">minimum_stock: {product.minimum_stock}</p>

                {/* Add a delete button */}
                <button onClick={() => handleDeleteProduct(product.id)} className="button">Delete</button>
              </div>
            </div>
          ))
        )}
      </div>
    </div>
  );
};

export default ProductList;
