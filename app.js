const express = require('express');
const helmet = require('helmet');
const authRoutes = require('./routes/auth');
const sequelize = require('./config/database');

const app = express();

// Middleware
app.use(express.json());
app.use(helmet());

// Routes
app.use('/auth', authRoutes);

// Sync Database
sequelize.sync()
    .then(() => console.log('Database connected and synced'))
    .catch(err => console.error('Error connecting to the database:', err));

module.exports = app;