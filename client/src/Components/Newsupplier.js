import React,{useState} from "react";
import './Newsupplier.css'

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
      logo: image,
    };
    addSupplier(newSupplier);
    // Clear the input fields
    setName("");
    setContact("");
    setimage("");
  };
  


  return (
    <div className="supplier-form-container">
      <h1>New Supplier</h1>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label className="label" htmlFor="name">
            Name:
          </label>
          <input
            className="input-field"
            type="text"
            id="name"
            name="name"
            value={name}
            onChange={handleNameChange}
            required
          />
        </div>
        <div className="form-group">
          <label className="label" htmlFor="contact">
            Contact:
          </label>
          <input
            className="input-field"
            type="text"
            id="contact"
            name="contact"
            value={contact}
            onChange={handleContactChange}
            required
          />
        </div>
        <div className="form-group">
          <label className="label" htmlFor="image">
            Image URL:
          </label>
          <input
            className="input-field"
            type="text"
            id="image"
            name="image"
            value={image}
            onChange={handleImageChange}
            required
          />
        </div>
        
        <button className="button" type="submit">
          Add Supplier
        </button>
      </form>
    </div>
  );
}

export default NewSupplier