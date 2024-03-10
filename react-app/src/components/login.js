import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import {useContext} from 'react';

const Login = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();
  const usernames = useContext({
    username,
    password 
  });


  const handleLogin = async () => {
   let data = {
    username,
    password,
  };

  try {
    const response = await axios.post('http://127.0.0.1:8000/app/login', data);
    console.log(response.data);
  } catch (error) {
    console.error("Error:", error);
  }
  };

  const navigateToRegister = () => {
    navigate('/register');
  };

  return (
    <div className="login-container">
      <h2>Login</h2>
      <form>
        <label htmlFor="username">Username:</label>
        <input
          type="text"
          id="username"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
        />

        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
        />

        <button type="button" onClick={handleLogin}>
          Login
        </button>
        <p>If you have not registered yet. <button type="button" onClick={navigateToRegister}>ClickMe</button></p>
      </form>
    </div>
  );
};

export default Login;
