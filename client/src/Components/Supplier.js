import React ,{ useEffect, useState } from 'react'
import SupplierList from './SupplierList';
import './Body.css';

 function Supplier() {
    const[suppliers ,setsuppliers]=useState([])
    useEffect(() => {
      fetch(' http://localhost:8000/suppliers')
        .then((r) => r.json())
        .then((data) => {setsuppliers(data)
        console.log(data)});
    }, []);
  return < >
  <h1>Suppliers</h1>
  <SupplierList suppliers={suppliers}/>
  </>;
}
export default Supplier;