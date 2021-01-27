import React from 'react'
import './Footer.css';
import { Navbar } from 'react-bootstrap';
import Button from './Button';

const Footer = () => {
   let year = new Date().getFullYear();
   return (
      <div className="footer">
        <Navbar className="justify-content-center">
         <Button id="game-rules" background="white" text={"game rules"} />
        </Navbar>
        <hr style={{marginTop: 0}}/>  {/*inline sttling*/}

        <p>This site has been created by Luca Di Molfetta and Walter Galante
          as an amateur project.
          <a href="mailto:dimolfetta.ta@gmail.com"> Write us</a> to report bugs. 
          &copy; WhaDoYM {year}
         </p>
      </div>
   )
}

export default Footer;
//#96267c