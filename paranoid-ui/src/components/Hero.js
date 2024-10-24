
import React from 'react';
import './Hero.css';  // Scoped styling for the hero component

const Hero = () => {
  return (
    <section className="hero">
      <div className="hero-content">
        <h1>Welcome to My Awesome App</h1>
        <p>Your journey to greatness begins here.</p>
        <a href="#get-started" className="cta-button">Get Started</a>
      </div>
    </section>
  );
};

export default Hero;
