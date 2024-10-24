
import React, { useState } from 'react';
import './ForgotPasswordComponent.css';

const ForgotPasswordComponent = () => {
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    setEmail(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);
    // Simulate password reset email
    setTimeout(() => {
      setMessage(`A password reset link has been sent to ${email}`);
      setLoading(false);
    }, 2000);  // Simulating a network call
  };

  return (
    <form className="forgot-password-form" onSubmit={handleSubmit}>
      <h2>Forgot Password</h2>
      <div className="form-group">
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          value={email}
          onChange={handleChange}
        />
      </div>
      <button type="submit" disabled={loading}>
        {loading ? 'Sending...' : 'Send Password Reset Email'}
      </button>
      {message && <p className="message">{message}</p>}
    </form>
  );
};

export default ForgotPasswordComponent;
