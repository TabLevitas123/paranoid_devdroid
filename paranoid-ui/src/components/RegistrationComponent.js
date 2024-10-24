
import React, { useState } from 'react';
import './RegistrationComponent.css';

const RegistrationComponent = ({ onRegisterSuccess }) => {
  const [formData, setFormData] = useState({
    email: '',
    password: '',
    confirmPassword: ''
  });

  const [errors, setErrors] = useState({
    email: '',
    password: '',
    confirmPassword: ''
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

    if (name === 'confirmPassword' && value !== formData.password) {
      setErrors({ ...errors, confirmPassword: 'Passwords do not match' });
    } else if (name === 'confirmPassword') {
      setErrors({ ...errors, confirmPassword: '' });
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (!errors.email && !errors.password && !errors.confirmPassword) {
      setLoading(true);
      // Simulating user registration and token generation
      setTimeout(() => {
        const mockJwtToken = 'new-user-jwt-token';  // In a real-world app, replace this with an API call
        localStorage.setItem('jwtToken', mockJwtToken);  // Store the JWT in localStorage
        onRegisterSuccess();
        setLoading(false);
      }, 2000);  // Simulating network delay
    }
  };

  return (
    <form className="registration-form" onSubmit={handleSubmit}>
      <h2>Register</h2>
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
      <div className="form-group">
        <label htmlFor="confirmPassword">Confirm Password:</label>
        <input
          type="password"
          id="confirmPassword"
          name="confirmPassword"
          value={formData.confirmPassword}
          onChange={handleChange}
        />
        {errors.confirmPassword && <span className="error">{errors.confirmPassword}</span>}
      </div>
      <button type="submit" disabled={loading || !!(errors.email || errors.password || errors.confirmPassword)}>
        {loading ? 'Registering...' : 'Register'}
      </button>
    </form>
  );
};

export default RegistrationComponent;
