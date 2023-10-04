import React from 'react';
import './Body.css';
import CardItem from './CardItem';

function Body() {
  return (
    <div className='cards'>
      <h1>Products</h1>
      <div className='cards__container'>
        <div className='cards__wrapper'>
          <ul className='cards__items'>
            <CardItem
              src='https://www.apple.com/newsroom/images/product/watch/standard/Apple_watch-series7_hero_09142021_big.jpg.slideshow-xlarge_2x.jpg'
              text='Apple Watch Series'
              label='Apple'
              path='/Products'
            />
            <CardItem
              src='https://i.ebayimg.com/images/g/xFcAAOSwyqNkcnJG/s-l1200.jpg'
              text='Surface Laptop 5'
              label='Microsoft'
              path='/Products'
            />
          </ul>
          <ul className='cards__items'>
            <CardItem
              src='https://img.global.news.samsung.com/ca/wp-content/uploads/2023/02/Samsung-Galaxy-S23-Image_1-799x563.png'
              text='Samsung Galaxy S23 series'
              label='Samsung'
              path='/Products'
            />
            <CardItem
              src='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRXxE-D2d9o-V4ZjlJrISI8V-uTgURtxkNhXOK4lL9shQ&s'
              text='Chromebook plus'
              label='Google'
              path='/Products'
            />
            <CardItem
              src='https://www.trustedreviews.com/wp-content/uploads/sites/54/2021/07/Huawei-Vision-S-Celia-1024x683.jpg'
              text='Huawei Vision 3 smart tv'
              label='Huawei'
              path='/Products'
            />
          </ul>
        </div>
      </div>
    </div>
  );
}

export default Body;
