
import React from 'react';
import './Navbar.css';  // Separate CSS file for scoped styling

const Navbar = () => {
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
    </nav>
  );
};

export default Navbar;
