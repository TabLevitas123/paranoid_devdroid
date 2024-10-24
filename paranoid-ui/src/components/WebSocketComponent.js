
import React, { useState, useEffect } from 'react';

const WebSocketComponent = () => {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    // Open WebSocket connection
    const ws = new WebSocket('wss://example-websocket-server.com/socket');  // Replace with actual WebSocket URL

    // Listen for messages
    ws.onmessage = (event) => {
      const message = JSON.parse(event.data);
      setMessages((prevMessages) => [...prevMessages, message]);
    };

    // Cleanup on unmount
    return () => {
      ws.close();
    };
  }, []);

  return (
    <div className="websocket-container">
      <h2>Real-Time Notifications</h2>
      <ul>
        {messages.map((msg, index) => (
          <li key={index}>{msg.text}</li>
        ))}
      </ul>
    </div>
  );
};

export default WebSocketComponent;
