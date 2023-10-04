import React from 'react';


const ProductList = ({ suppliers }) => {
  
  
  
zzz
 


  return (
    <div className='Suppliers'>
      
     
     
      
      <div className='cardiis ' >
        
          {suppliers.map((suppier) => (
            <div key={suppier.id} className='cards__item__link'>
                <figure className='cards__item__pic-wrap'>
              <img  className='cards__item__img'src={suppier.logo} alt="Your suppier" />
              </figure>
              <div className='cards__item__info'>
                <h5 className='cards__item__text'>{suppier.name}</h5>
                <p>{suppier.contact}</p>
              </div>
            </div>
          ))}
    
      </div>
      
    </div>
  );
};

export default ProductList;