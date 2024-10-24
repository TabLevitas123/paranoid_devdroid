
import React from 'react';
import { useHistory } from 'react-router-dom';

const LogoutComponent = () => {
  const history = useHistory();

  const handleLogout = () => {
    localStorage.removeItem('jwtToken');  // Remove the JWT token
    history.push('/login');  // Redirect to login page
  };

  return (
    <button onClick={handleLogout}>
      Logout
    </button>
  );
};

export default LogoutComponent;
