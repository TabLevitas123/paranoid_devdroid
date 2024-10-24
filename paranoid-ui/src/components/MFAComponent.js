
import React, { useState } from 'react';
import './MFAComponent.css';

const MFAComponent = ({ onMFASuccess }) => {
  const [code, setCode] = useState('');
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(false);
  const [verificationCode, setVerificationCode] = useState('123456');  // Mock verification code

  const handleChange = (e) => {
    setCode(e.target.value);
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);
    // Simulating code verification
    setTimeout(() => {
      if (code === verificationCode) {
        setMessage('Verification successful!');
        onMFASuccess();
      } else {
        setMessage('Invalid verification code.');
      }
      setLoading(false);
    }, 2000);  // Simulating a network delay
  };

  return (
    <form className="mfa-form" onSubmit={handleSubmit}>
      <h2>Multi-factor Authentication</h2>
      <p>A verification code has been sent to your email/phone. Please enter the code below:</p>
      <div className="form-group">
        <label htmlFor="code">Verification Code:</label>
        <input
          type="text"
          id="code"
          name="code"
          value={code}
          onChange={handleChange}
        />
      </div>
      <button type="submit" disabled={loading}>
        {loading ? 'Verifying...' : 'Verify'}
      </button>
      {message && <p className="message">{message}</p>}
    </form>
  );
};

export default MFAComponent;
