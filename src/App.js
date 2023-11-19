import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import "./App.css";
import Homepage from './components/homepage/homepage';
import Login from './components/login/login';
import Register from './components/register/register';

function App() {
  const [user, setLoginUser] = useState({});

  return (
    <div className="App">
      <Router>
        <Routes>
          {user && user._id ? (
            <Route path="/" element={<Homepage setLoginUser={setLoginUser} />} />
          ) : (
            <>
              <Route path="/" element={<Login setLoginUser={setLoginUser} />} />
              <Route path="/login" element={<Login setLoginUser={setLoginUser} />} />
              <Route path="/register" element={<Register />} />
            </>
          )}
        </Routes>
      </Router>
  <div className="title">
  <h5>AgriConnect</h5>
  <h3><pre> -An Agricultural Decision Support System.</pre></h3>
  </div>
    </div>

  );
}

export default App;