import React,{useState} from "react";
import { useParams } from "react-router-dom";
import './Form.css'

function NewProduct({ addProduct }){
  const { supplierId } = useParams(); // Get the supplierId from the URL params
  const [product_name, setProduct_name] = useState("");
  const [type, setType] = useState("");
  const [image, setImage] = useState("");
  const [quantity, setQuantity] = useState("");
  const [minimum_stock, setMinimum_stock] = useState("");
  const [description, setDescription] = useState("");




  const handleProduct_nameChange = (event) => {
    setProduct_name(event.target.value);
  };
  const handleDescriptionChange = (event) => {
    setDescription(event.target.value);
  };
  const handleQuantityChange= (event) => {
    setQuantity(event.target.value);
  };
  const handleMinimum_stockChange= (event) => {
    setMinimum_stock(event.target.value);
  };


  const handleTypeChange = (event) => {
    setType(event.target.value);
  };
  const handleImageChange = (event) => {
    setImage(event.target.value);
  };


  

  const handleSubmit = (event) => {
    event.preventDefault();
    // Create a new Product object using the form data
    const newProduct = {
      product_name: product_name, // Use lowercase attribute product_names
      type: type, // Use lowercase attribute product_names
      image: image,
      quantity: quantity,
      minimum_stock: minimum_stock,
      description: description
    };
    addProduct(supplierId,newProduct);
    // Clear the input fields
    setProduct_name("");
    setType("");
    setImage("");
    setDescription("");
  };
  


    return(
      <>
    <div className="new-product-container">
      <h1>New Product</h1>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label className="label" htmlFor="product_name">
            Product Name:
          </label>
          <input
            className="input-field"
            type="text"
            id="product_name"
            name="product_name"
            value={product_name}
            onChange={handleProduct_nameChange}
            required
          />
          <label className="label" htmlFor="product_name">
           Description:
          </label>
          <input
            className="input-field"
            type="text"
            id="product_name"
            name="product_name"
            value={description}
            onChange={handleDescriptionChange}
            required
          />
        </div>
        <div className="form-group">
          <label className="label" htmlFor="type">
            Type:
          </label>
          <input
            className="input-field"
            type="text"
            id="type"
            name="type"
            value={type}
            onChange={handleTypeChange}
            required
          />
        </div>
        <div className="form-group">
          <label className="label" htmlFor="type">
              Minimum_stock:
          </label>
          <input
            className="input-field"
            type="text"
            id="type"
            name="type"
            value={minimum_stock}
            onChange={handleMinimum_stockChange}
            required
          />
        </div>
        <div className="form-group">
          <label className="label" htmlFor="type">
            Quantity:
          </label>
          <input
            className="input-field"
            type="text"
            id="type"
            name="type"
            value={quantity}
            onChange={handleQuantityChange}
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
          Add Product
        </button>
      </form>
    </div>
        </>
    )
}
export default NewProduct