
import React, { useState } from 'react';
import './EmailNotificationComponent.css';

const EmailNotificationComponent = () => {
  const [notifications, setNotifications] = useState([]);

  const triggerNotification = (type) => {
    const notificationMessage = `Email notification: ${type} event occurred.`;
    setNotifications((prev) => [...prev, notificationMessage]);
  };

  return (
    <div className="email-notification-container">
      <h2>Email Notifications</h2>
      <button onClick={() => triggerNotification('Login attempt')}>
        Simulate Login Notification
      </button>
      <button onClick={() => triggerNotification('Password change')}>
        Simulate Password Change Notification
      </button>
      <ul>
        {notifications.map((notification, index) => (
          <li key={index}>{notification}</li>
        ))}
      </ul>
    </div>
  );
};

export default EmailNotificationComponent;
