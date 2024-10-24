
import React, { useState, useEffect } from 'react';
import './Navbar.css';  // Separate CSS file for scoped styling

const Navbar = () => {
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    // Load the saved theme from localStorage
    const savedTheme = localStorage.getItem('darkMode') === 'true';
    setDarkMode(savedTheme);
    document.body.classList.toggle('dark-theme', savedTheme);
  }, []);

  const toggleTheme = () => {
    setDarkMode(!darkMode);
    localStorage.setItem('darkMode', !darkMode);  // Save the theme preference to localStorage
    document.body.classList.toggle('dark-theme', !darkMode);
  };

  return (
    <nav className="navbar">
      <div className="navbar-logo">
        <a href="/">My App</a>
      </div>
      <ul className="navbar-links">
        <li><a href="#about">About</a></li>
        <li><a href="#services">Services</a></li>
        <li><a href="#contact">Contact</a></li>
      </ul>
      <div className="navbar-toggle">
        <button className="toggle-button">Menu</button>
      </div>
      <button className="theme-toggle" onClick={toggleTheme}>
        {darkMode ? 'Light Mode' : 'Dark Mode'}
      </button>
    </nav>
  );
};

export default Navbar;
