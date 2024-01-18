import React, { useEffect, useState } from 'react';
import SupplierList from './SupplierList';
import './Body.css';
import NewSupplier from './Newsupplier'; 

function Supplier({access_token,headers}) {
  const [suppliers, setsuppliers] = useState([]);
  const [showNewSupplier, setShowNewSupplier] = useState(false); // State variable to control the visibility of NewSupplier

  useEffect(() => {
    fetch('http://127.0.0.1:5555/suppliers',{  method: 'GET', 
    headers: headers,
  })
      .then((r) => r.json())
      .then((data) => {
        setsuppliers(data);
        console.log(data);
      });
  }, []);

  const addSupplier = (newSupplier) => {
    // Make a POST request to add a new supplier to the database
    fetch('http://127.0.0.1:5555/suppliers', {
      method: 'POST',
      headers: {
        'Authorization': `Bearer ${access_token}`,
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(newSupplier), // Convert the newSupplier object to JSON
    })
      .then((response) => response.json())
      .then((data) => {
        // Handle the response if needed
        console.log(data);

        // Add the new supplier to the local state
        setsuppliers([...suppliers, data]);
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  };

  return (
    <>
      <h1>Suppliers</h1>
      {/* Button to toggle the NewSupplier component */}
      <button onClick={() => setShowNewSupplier(!showNewSupplier)} className='hide'>
        {showNewSupplier ? 'Hide form' : 'Add New Supplier'}
      </button>
      
      {/* Conditional rendering of the NewSupplier component */}
      {showNewSupplier && <NewSupplier addSupplier={addSupplier} />}
      <SupplierList suppliers={suppliers} />
    </>
  );
}

export default Supplier;
