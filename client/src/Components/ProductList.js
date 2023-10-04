import React, { useState } from 'react';


const ProductList = ({ products }) => {
  const [selectedCategory, setSelectedCategory] = useState('all');
 
  
  // Function to filter the Products based on the selected category
  const filterProducts = (category) => {
    setSelectedCategory(category);
  };

  // Filter the Products based on the selected category
  const filteredProducts = selectedCategory === 'all' ? products : products.filter((product) => product.Category === selectedCategory);

  
  // Function to remove an product from the wishlist
  



  return (
    <div className='Products'>
      <div className="filter-buttons">
        <button onClick={() => filterProducts('all')}>All</button>
        <button onClick={() => filterProducts('Laptop')}>Laptops</button>
        <button onClick={() => filterProducts('Phone')}>Phone</button>
        
      </div>
     
      
      <div className='cardis ' >
        {filteredProducts.length === 0 ? (
          <div className="col-12">
            <h2 style={{color:"white"}}>No Matches Found</h2>
          </div>
        ) : (
          filteredProducts.map((product) => (
            <div key={product.id} className='cards__item__link'>
                <figure className='cards__item__pic-wrap'>
              <img  className='cards__item__img'src={product.image} alt="Your product" />
              </figure>
              <div className='cards__item__info'>
                <h5 className='cards__item__text'>{product.product_name}</h5>
                
                <p className='cards__item__text'>{product.type}</p>
                <p className='cards__item__text'>quantity: {product.quantity}</p>
                <p className='cards__item__text'>minimum_stock: {product.minimum_stock}</p>

              </div>
            </div>
          ))
        )}
      </div>
      
    </div>
  );
};

export default ProductList;