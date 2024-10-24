
import React, { useState } from 'react';
import './LoginComponent.css';

const LoginComponent = ({ onLoginSuccess }) => {
  const [formData, setFormData] = useState({
    email: '',
    password: ''
  });

  const [errors, setErrors] = useState({
    email: '',
    password: ''
  });

  const [loading, setLoading] = useState(false);

  const validateEmail = (email) => {
    const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(String(email).toLowerCase());
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });

    // Real-time validation
    if (name === 'email' && !validateEmail(value)) {
      setErrors({ ...errors, email: 'Invalid email address' });
    } else if (name === 'email') {
      setErrors({ ...errors, email: '' });
    }

    if (name === 'password' && value.length < 6) {
      setErrors({ ...errors, password: 'Password must be at least 6 characters' });
    } else if (name === 'password') {
      setErrors({ ...errors, password: '' });
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!errors.email && !errors.password) {
      setLoading(true);
      // Mock API call for JWT authentication
      setTimeout(() => {
        const mockJwtToken = 'fake-jwt-token';  // In a real-world app, you'd replace this with an actual API call
        localStorage.setItem('jwtToken', mockJwtToken);  // Store the JWT in localStorage
        onLoginSuccess();
        setLoading(false);
      }, 2000);  // Simulating network delay
    }
  };

  return (
    <form className="login-form" onSubmit={handleSubmit}>
      <h2>Login</h2>
      <div className="form-group">
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
        />
        {errors.email && <span className="error">{errors.email}</span>}
      </div>
      <div className="form-group">
        <label htmlFor="password">Password:</label>
        <input
          type="password"
          id="password"
          name="password"
          value={formData.password}
          onChange={handleChange}
        />
        {errors.password && <span className="error">{errors.password}</span>}
      </div>
      <button type="submit" disabled={loading || !!(errors.email || errors.password)}>
        {loading ? 'Logging in...' : 'Login'}
      </button>
    </form>
  );
};

export default LoginComponent;
