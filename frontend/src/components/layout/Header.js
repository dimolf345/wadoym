import React, { Component } from 'react';
import {Nav, Navbar} from 'react-bootstrap';


class Header extends React.Component {
   render() {
      return (
         <div>
            <Navbar bg="dark" expand="lg">
               <h1>Porco dio</h1>
            </Navbar> 
         </div>
      )
   }
}
export default Header;
