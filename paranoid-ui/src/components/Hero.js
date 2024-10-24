
import React from 'react';
import { Container, Typography, Button } from '@mui/material';
import { motion } from 'framer-motion';

const Hero = () => {
  return (
    <Container>
      <motion.div
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ duration: 1 }}
      >
        <Typography variant="h2" gutterBottom>
          Welcome to Paranoid Devdroid
        </Typography>
        <Typography variant="h6" paragraph>
          The most advanced, modern, and minimalist UI to date!
        </Typography>
        <Button variant="contained" color="primary" href="#learn-more">
          Learn More
        </Button>
      </motion.div>
    </Container>
  );
};

export default Hero;
