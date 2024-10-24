
import React, { useState, useEffect } from 'react';
import './UserProfileComponent.css';

const UserProfileComponent = () => {
  const [profile, setProfile] = useState({
    email: 'user@example.com',  // Simulated user data
    password: ''
  });
  const [newPassword, setNewPassword] = useState('');
  const [message, setMessage] = useState('');
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    // Simulating fetching user profile data (could be replaced with an actual API call)
    setProfile({
      email: 'user@example.com',
      password: '********'  // Hide the actual password
    });
  }, []);

  const handleChange = (e) => {
    const { name, value } = e.target;
    if (name === 'newPassword') {
      setNewPassword(value);
    } else {
      setProfile({ ...profile, [name]: value });
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    setLoading(true);
    // Simulate profile update
    setTimeout(() => {
      setMessage('Profile updated successfully!');
      setLoading(false);
    }, 2000);  // Simulating a network delay
  };

  return (
    <form className="profile-form" onSubmit={handleSubmit}>
      <h2>User Profile</h2>
      <div className="form-group">
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          value={profile.email}
          onChange={handleChange}
        />
      </div>
      <div className="form-group">
        <label htmlFor="password">Current Password:</label>
        <input
          type="password"
          id="password"
          name="password"
          value={profile.password}
          disabled  // Current password cannot be changed directly
        />
      </div>
      <div className="form-group">
        <label htmlFor="newPassword">New Password:</label>
        <input
          type="password"
          id="newPassword"
          name="newPassword"
          value={newPassword}
          onChange={handleChange}
        />
      </div>
      <button type="submit" disabled={loading}>
        {loading ? 'Updating...' : 'Update Profile'}
      </button>
      {message && <p className="message">{message}</p>}
    </form>
  );
};

export default UserProfileComponent;
