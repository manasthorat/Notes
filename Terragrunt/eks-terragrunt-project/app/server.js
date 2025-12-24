const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

// Simple health check endpoint
app.get('/health', (req, res) => {
  res.status(200).json({ status: 'healthy' });
});

// Main endpoint
app.get('/', (req, res) => {
  res.json({ 
    message: 'Hello from EKS!',
    timestamp: new Date().toISOString(),
    hostname: require('os').hostname()
  });
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});