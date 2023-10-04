import React,{useState} from "react";

function NewSupplier({ addSupplier }){
  const [name, setName] = useState("");
  const [contact, setContact] = useState("");
  const [image, setimage] = useState("");
  


  const handleNameChange = (event) => {
    setName(event.target.value);
  };


  const handleContactChange = (event) => {
    setContact(event.target.value);
  };
  const handleImageChange = (event) => {
    setimage(event.target.value);
  };


  

  const handleSubmit = (event) => {
    event.preventDefault();
    // Create a new Supplier object using the form data
    const newSupplier = {
      name: name, // Use lowercase attribute names
      contact: contact, // Use lowercase attribute names
      image: image,
    };
    addSupplier(newSupplier);
    // Clear the input fields
    setName("");
    setContact("");
    setimage("");
  };
  


    return(
      <>
      <h1>New Supplier</h1>
        <form>
            <label>Name:</label>
            <input type="Name" value={name} onChange={handleNameChange} /><br></br>
            <label>Contact</label>
            <input type="text" value={contact} onChange={handleContactChange}/><br></br>
            <label>Image</label>
            <input type="text" value={image} onChange={handleImageChange}/><br></br>
            
            <button type="submit" onClick={handleSubmit }>Add Supplier</button><br></br>
        </form>
        </>
    )
}
export default NewSupplier