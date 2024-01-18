import React, { useState, useEffect } from "react";



function Outgoing() {
  const [shippings, setShippings] = useState([]);
  
//fetch the transcations
useEffect(() => {
  fetch("http://127.0.0.1:5555/shippings")
    .then((r) => r.json())
    .then((data) => {
      console.log("Fetched data:", data)
      //sort the fetched array alphabetically according to the category
     
      setShippings(data)
      });
     
},[]); 

  



  
  return  (
    <>
      <h1>Shippings</h1>
     
     
      {/*display transaction if description match and Transaction not found if there is no description that matches the search*/}
      {shippings.length === 0 ? (
        <p>Shippings not found</p>
      ) : (
        <table style={{ width: "70%" ,fontSize:"larger"}}>
          <thead>
           <tr>
           <th style={{ backgroundColor: "#f79771" }}>Product ID</th>
            <th style={{ backgroundColor: "#a29bfe" }}>Status</th>
            <th style={{ backgroundColor: "#74b9ff" }}>Created at</th>
            
            
      </tr>
          </thead>
          <tbody>
            {shippings.map((transaction) => (
              <tr key={transaction.id}>
                <td>{transaction.product_id}</td>
                <td>{transaction.status}</td>
                <td>{transaction.created_at}</td>
                
                
              </tr>
            ))}
          </tbody>
        </table>
      )}
     
    </>
  );
}
export default Outgoing
//http://127.0.0.1:5555/shippings