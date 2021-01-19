import React from 'react'
import { Navbar } from 'react-bootstrap';
import './Header.css';
import memehr from '../../assets/memehr.jpeg'; 

const Header = () => {
   return (
      <div className="header">
        <Navbar className="justify-content-center" bg="dark">
         <Navbar.Brand href="#home">
           <img
             src={memehr}
              alt="logo"
             />
         </Navbar.Brand>
         <h3 className="title">What do you meme online game</h3>   
  </Navbar>
      </div>
   )
}

export default Header;
//#96267c