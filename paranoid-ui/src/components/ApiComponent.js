
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './ApiComponent.css';

const ApiComponent = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const element = document.querySelector('.api-content');

    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            axios.get('https://jsonplaceholder.typicode.com/posts')
              .then(response => {
                setData(response.data.slice(0, 5));
                setLoading(false);  // Stop spinner when data is loaded
              })
              .catch(error => {
                console.error('Error fetching data:', error);
              });
          }
        });
      },
      { threshold: 0.1 }
    );

    observer.observe(element);
    
    return () => {
      if (element) observer.unobserve(element);
    };
  }, []);

  return (
    <div className="api-content">
      <h2>Live Data from API</h2>
      {loading ? (
        <div className="spinner">Loading...</div>  // Spinner during loading
      ) : (
        <ul>
          {data.map(item => (
            <li key={item.id}>
              <h3>{item.title}</h3>
              <p>{item.body}</p>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default ApiComponent;
