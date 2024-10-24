
import React, { useState, useEffect } from 'react';
import './WebSocketComponent.css';

const WebSocketComponent = () => {
  const [messages, setMessages] = useState([]);
  const [newAlert, setNewAlert] = useState(false);

  useEffect(() => {
    // Open WebSocket connection
    const ws = new WebSocket('wss://example-websocket-server.com/socket');  // Replace with actual WebSocket URL

    // Listen for messages
    ws.onmessage = (event) => {
      const message = JSON.parse(event.data);
      setMessages((prevMessages) => [...prevMessages, message]);
      setNewAlert(true);  // Trigger a new alert
      playNotificationSound();  // Play sound when a new message arrives
    };

    // Cleanup on unmount
    return () => {
      ws.close();
    };
  }, []);

  const playNotificationSound = () => {
    const audio = new Audio('/notification-sound.mp3');  // Make sure to add a sound file
    audio.play();
  };

  const closeAlert = () => {
    setNewAlert(false);  // Close the alert
  };

  return (
    <div className="websocket-container">
      <h2>Real-Time Notifications</h2>
      <ul>
        {messages.map((msg, index) => (
          <li key={index}>{msg.text}</li>
        ))}
      </ul>

      {newAlert && (
        <div className="alert-popup">
          <p>New message received!</p>
          <button onClick={closeAlert}>Close</button>
        </div>
      )}
    </div>
  );
};

export default WebSocketComponent;
