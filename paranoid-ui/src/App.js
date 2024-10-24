
import React from 'react';
import Navbar from './components/Navbar';
import Hero from './components/Hero';
import { ThemeProvider, createTheme, CssBaseline } from '@mui/material';
import { useState } from 'react';

function App() {
  const [darkMode, setDarkMode] = useState(false);
  
  const theme = createTheme({
    palette: {
      mode: darkMode ? 'dark' : 'light',
    },
  });

  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Navbar />
      <Hero />
      <button onClick={() => setDarkMode(!darkMode)}>Toggle Dark Mode</button>
    </ThemeProvider>
  );
}

export default App;
