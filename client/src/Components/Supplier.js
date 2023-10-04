import React, { useEffect, useState } from 'react';
import SupplierList from './SupplierList';
import './Body.css';
import NewSupplier from './Newsupplier'; 

function Supplier() {
  const [suppliers, setsuppliers] = useState([]);
  const [showNewSupplier, setShowNewSupplier] = useState(false); // State variable to control the visibility of NewSupplier

  useEffect(() => {
    fetch('http://127.0.0.1:5555/suppliers')
      .then((r) => r.json())
      .then((data) => {
        setsuppliers(data);
        console.log(data);
      });
  }, []);

  const addSupplier = (newSupplier) => {
    setsuppliers([...suppliers, newSupplier]);
  };

  return (
    <>
      <h1>Suppliers</h1>
      {/* Button to toggle the NewSupplier component */}
      <button onClick={() => setShowNewSupplier(!showNewSupplier)}>
        {showNewSupplier ? 'Hide form' : 'Add New Supplier'}
      </button>
      
      {/* Conditional rendering of the NewSupplier component */}
      {showNewSupplier && <NewSupplier addSupplier={addSupplier} />}
      <SupplierList suppliers={suppliers} />
    </>
  );
}

export default Supplier;
