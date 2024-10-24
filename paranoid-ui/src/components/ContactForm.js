
import React, { useState } from 'react';
import './ContactForm.css';

const ContactForm = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: ''
  });

  const [errors, setErrors] = useState({
    name: '',
    email: '',
    message: ''
  });

  const validateEmail = (email) => {
    const re = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    return re.test(String(email).toLowerCase());
  };

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });

    // Real-time validation logic
    if (name === 'email' && !validateEmail(value)) {
      setErrors({ ...errors, email: 'Invalid email address' });
    } else if (name === 'email') {
      setErrors({ ...errors, email: '' });
    }

    if (name === 'name' && value.trim() === '') {
      setErrors({ ...errors, name: 'Name is required' });
    } else if (name === 'name') {
      setErrors({ ...errors, name: '' });
    }

    if (name === 'message' && value.trim() === '') {
      setErrors({ ...errors, message: 'Message is required' });
    } else if (name === 'message') {
      setErrors({ ...errors, message: '' });
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // Additional submission logic here
    alert('Form submitted successfully!');
  };

  return (
    <form className="contact-form" onSubmit={handleSubmit}>
      <h2>Contact Us</h2>
      <div className="form-group">
        <label htmlFor="name">Name:</label>
        <input
          type="text"
          id="name"
          name="name"
          value={formData.name}
          onChange={handleChange}
        />
        {errors.name && <span className="error">{errors.name}</span>}
      </div>
      <div className="form-group">
        <label htmlFor="email">Email:</label>
        <input
          type="email"
          id="email"
          name="email"
          value={formData.email}
          onChange={handleChange}
        />
        {errors.email && <span className="error">{errors.email}</span>}
      </div>
      <div className="form-group">
        <label htmlFor="message">Message:</label>
        <textarea
          id="message"
          name="message"
          value={formData.message}
          onChange={handleChange}
        ></textarea>
        {errors.message && <span className="error">{errors.message}</span>}
      </div>
      <button type="submit" disabled={!!(errors.name || errors.email || errors.message)}>
        Submit
      </button>
    </form>
  );
};

export default ContactForm;
