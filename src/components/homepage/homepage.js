import React from "react"
import "./homepage.css"

const Homepage = ({setLoginUser}) => {
    const WeatherStreamlitApp = () => {
        // Replace 'http://localhost:8501' with the actual URL where your Streamlit app is running
        window.open('http://localhost:8501','_blank') ;
    };
    const YieldStreamlitApp = () => {
        // Replace 'http://localhost:8501' with the actual URL where your Streamlit app is running
        window.open('http://localhost:8502','_blank') ;
    };
    const PestStreamlitApp = () => {
        // Replace 'http://localhost:8501' with the actual URL where your Streamlit app is running
        window.open('http://localhost:8503','_blank') ;
    };
    return (
        <div className="homepage">
            <h1>Welcome !</h1>
            <br></br>
            <br></br>
            <div className="button" onClick={WeatherStreamlitApp}>Weather Prediction</div>
            <div className="button" onClick={YieldStreamlitApp}>Yield Prediction</div>
            <div className="button" onClick={PestStreamlitApp}>Pest Classification</div>
            <br></br>
            <br></br>
            <div className="button" onClick={() => setLoginUser({})} >Logout</div>
        </div>
    )
}

export default Homepage