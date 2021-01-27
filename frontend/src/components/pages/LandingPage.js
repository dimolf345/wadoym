import React from 'react';
import './LandingPage.css'
import image from '../../assets/landingmeme.png';
import PlayerForm from '../layout/PlayerForm';

class LandingPage extends React.Component {

    render() {
        return (
        //divides the landing page in two columns
        <div className="main-content">
            <div className="column left">
                <img src={image} alt=""/>
            </div>
            <div className="column right">
                <PlayerForm/>
            </div>
        </div>
         ) //form colum will be updated
    }
}


export default LandingPage;
