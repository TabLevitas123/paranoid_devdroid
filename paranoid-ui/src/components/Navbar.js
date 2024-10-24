
import React from 'react';
import { AppBar, Toolbar, IconButton, Typography, Button } from '@mui/material';
import MenuIcon from '@mui/icons-material/Menu';
import { motion } from 'framer-motion';

const Navbar = () => {
  return (
    <motion.div initial={{ y: -100 }} animate={{ y: 0 }}>
      <AppBar position="static">
        <Toolbar>
          <IconButton edge="start" color="inherit" aria-label="menu">
            <MenuIcon />
          </IconButton>
          <Typography variant="h6" style={{ flexGrow: 1 }}>
            Paranoid Devdroid
          </Typography>
          <Button color="inherit">Login</Button>
        </Toolbar>
      </AppBar>
    </motion.div>
  );
};

export default Navbar;
