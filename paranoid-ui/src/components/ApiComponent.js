
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './ApiComponent.css';  // Scoped CSS for the component

const ApiComponent = () => {
  const [data, setData] = useState([]);
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const element = document.querySelector('.api-content');

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            setIsVisible(true);
            observer.disconnect();  // Stop observing after it's visible
          }
        });
      },
      { threshold: 0.1 }  // Trigger when 10% of the element is visible
    );

    observer.observe(element);
    
    return () => {
      if (element) observer.unobserve(element);
    };
  }, []);

  useEffect(() => {
    if (isVisible) {
      axios.get('https://jsonplaceholder.typicode.com/posts')
        .then(response => {
          setData(response.data.slice(0, 5));  // Limiting to 5 posts for brevity
        })
        .catch(error => {
          console.error('Error fetching data:', error);
        });
    }
  }, [isVisible]);

  return (
    <div className="api-content">
      <h2>Live Data from API</h2>
      {isVisible ? (
        <ul>
          {data.map(item => (
            <li key={item.id}>
              <h3>{item.title}</h3>
              <p>{item.body}</p>
            </li>
          ))}
        </ul>
      ) : (
        <p>Loading...</p>
      )}
    </div>
  );
};

export default ApiComponent;
