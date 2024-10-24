
import React, { useEffect } from 'react';
import './App.css';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import ApiComponent from './components/ApiComponent';

function App() {
  useEffect(() => {
    const scrollElements = document.querySelectorAll('.fade-in-up, .fade-in-left');
    
    const elementInView = (el, dividend = 1) => {
      const elementTop = el.getBoundingClientRect().top;
      return (
        elementTop <= (window.innerHeight || document.documentElement.clientHeight) / dividend
      );
    };

    const displayScrollElement = (element) => {
      element.classList.add('active');
    };

    const handleScrollAnimation = () => {
      scrollElements.forEach((el) => {
        if (elementInView(el, 1.25)) {
          displayScrollElement(el);
        }
      });
    };

    window.addEventListener('scroll', () => {
      handleScrollAnimation();
    });

    return () => {
      window.removeEventListener('scroll', handleScrollAnimation);
    };
  }, []);

  return (
    <div className="App">
      <Navbar />
      <div className="fade-in-up">
        <Hero />
      </div>
      <div className="fade-in-left">
        <ApiComponent />
      </div>
    </div>
  );
}

export default App;
