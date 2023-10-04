import React, { useState } from 'react';


const ProductList = ({ areas }) => {
  const [selectedCategory, setSelectedCategory] = useState('all');
 
  
  // Function to filter the areas based on the selected category
  const filterAreas = (category) => {
    setSelectedCategory(category);
  };

  // Filter the areas based on the selected category
  const filteredAreas = selectedCategory === 'all' ? areas : areas.filter((area) => area.Category === selectedCategory);

  
  // Function to remove an area from the wishlist
  



  return (
    <div className='Areas'>
      <div className="filter-buttons">
        <button onClick={() => filterAreas('all')}>All</button>
        <button onClick={() => filterAreas('parks')}>Park</button>
        <button onClick={() => filterAreas('mall')}>Mall</button>
        <button onClick={() => filterAreas('historic site')}>Historic</button>
        <button onClick={() => filterAreas('Beach')}>Beach</button>
        <button onClick={() => filterAreas('Hotel')}>Hotel</button>
      
      </div>
     
      
      <div className='cardis ' >
        {filteredAreas.length === 0 ? (
          <div className="col-12">
            <h2 style={{color:"white"}}>No Matches Found</h2>
          </div>
        ) : (
          filteredAreas.map((area) => (
            <div key={area.id} className='cards__item__link'>
                <figure className='cards__item__pic-wrap'>
              <img  className='cards__item__img'src={area.image} alt="Your area" />
              </figure>
              <div className='cards__item__info'>
                <h5 className='cards__item__text'>{area.name}</h5>
              </div>
            </div>
          ))
        )}
      </div>
      
    </div>
  );
};

export default ProductList;