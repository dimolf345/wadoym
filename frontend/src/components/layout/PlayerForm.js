import React from "react";
import './PlayerForm.css';
import Button from './Button';

const FormPage = () => {
return (
    <div className="form-container">
      <form>
        <input id="userName" type="text" label="userName" placeholder="Enter your name"/>
        <input id="nickName" type="text" label="nickName" placeholder="Enter your nick name"/>
        <h4>Let's Play!</h4>
        <hr/>
        <div className="button-area">
        <Button background={"melange"} text={"create a game"}/> 
        <Button background={"cool"} text={"join a game"} />
        </div>
        <hr/>
        </form>
      </div>
    );
};

export default FormPage;