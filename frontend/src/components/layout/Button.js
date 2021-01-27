import React from 'react'
import './Button.css'

const Button = ({background, text, id=''}) => {
    if(background==="melange" || background==="cool" ) {background="var(--"+background+")"};
    return(
        <div id={id} className="button-container">
            <button style= {{backgroundColor: background}}>
            {text}
            </button>
        </div>
    )
}



export default Button;