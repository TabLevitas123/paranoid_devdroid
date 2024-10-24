
import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './ApiComponent.css';  // Scoped CSS for the component

const ApiComponent = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    // Fetching data from an example API
    axios.get('https://jsonplaceholder.typicode.com/posts')
      .then(response => {
        setData(response.data.slice(0, 5));  // Limiting to 5 posts for brevity
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }, []);

  return (
    <div className="api-content">
      <h2>Live Data from API</h2>
      <ul>
        {data.map(item => (
          <li key={item.id}>
            <h3>{item.title}</h3>
            <p>{item.body}</p>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ApiComponent;
