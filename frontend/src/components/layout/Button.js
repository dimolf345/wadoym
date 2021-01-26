import React from 'react'
import './Button.css'

const Button = ({background, text}) => {
    background="var(--"+background+")";
    return(
        <div className="button-container">
            <button style= {{backgroundColor: background}}>
            {text}
            </button>
        </div>
    )
}



export default Button;