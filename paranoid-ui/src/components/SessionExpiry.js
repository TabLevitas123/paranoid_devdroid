
import React, { useEffect } from 'react';
import { useHistory } from 'react-router-dom';

const SessionExpiry = ({ timeout = 900000 }) => {  // Default timeout set to 15 minutes (900,000 ms)
  const history = useHistory();

  useEffect(() => {
    let logoutTimer;

    const resetTimer = () => {
      clearTimeout(logoutTimer);  // Clear the previous timer
      logoutTimer = setTimeout(() => {
        handleLogout();  // Logout the user after the timeout period
      }, timeout);
    };

    const handleLogout = () => {
      localStorage.removeItem('jwtToken');  // Remove the JWT token
      history.push('/login');  // Redirect to login page
      alert('You have been logged out due to inactivity.');
    };

    // Detect user activity (mouse move, keypress, click, etc.)
    window.addEventListener('mousemove', resetTimer);
    window.addEventListener('keypress', resetTimer);
    window.addEventListener('click', resetTimer);

    // Start the timer when the component mounts
    resetTimer();

    // Cleanup event listeners on component unmount
    return () => {
      clearTimeout(logoutTimer);
      window.removeEventListener('mousemove', resetTimer);
      window.removeEventListener('keypress', resetTimer);
      window.removeEventListener('click', resetTimer);
    };
  }, [history, timeout]);

  return null;  // No UI element is needed for this component
};

export default SessionExpiry;
