import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const Register = () => {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const navigate = useNavigate();

  const handleRegister = async () => {
    if (password !== confirmPassword) {
      alert("Passwords do not match");
      return;
    }

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

    console.log('Register clicked!');
  };

  const navigateToLogin = () => {
    navigate('/login');
  };

  return (
    <div className="register-container">
      <h2>Register</h2>
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

        <label htmlFor="confirmPassword">Confirm Password:</label>
        <input
          type="password"
          id="confirmPassword"
          value={confirmPassword}
          onChange={(e) => setConfirmPassword(e.target.value)}
        />

        <button type="button" onClick={handleRegister}>
          Register
        </button>
        <p>If you have already registered. <button type="button" onClick={navigateToLogin}>ClickMe</button></p>
      </form>
    </div>
  );
};

export default Register;
