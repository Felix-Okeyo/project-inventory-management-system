import React, { useState } from "react";

function Searchbar({ onSearch }) {
  const [type, setType] = useState("");

  function handleSearch(event) {
    setType(event.target.value);
    // Pass the entered description back to the parent component
    onSearch(event.target.value);
    console.log(event.target.value)
  }

  return (
    <form>
    <input
      type="text"
      placeholder="search product type"
      value={type}
      onChange={handleSearch}
    />
    <i className="fa fa-search"></i>
    </form>
  );
}

export default Searchbar;