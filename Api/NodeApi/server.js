const express = require('express');
const mysql = require('mysql2');
const bodyParser = require('body-parser');

const app = express();
const port = 3000;

// Middleware
app.use(bodyParser.json());

// Create a MySQL connection pool
const pool = mysql.createPool({
    host: 'localhost',
    user: 'root',
    password: 'root',
    database: 'project_IOT'  // Ensure this matches your existing database name
});

// Get all persons
app.get('/persons', (req, res) => {
    pool.query('SELECT * FROM person', (err, results) => {
        if (err) return res.status(500).send(err);
        res.json(results);
    });
});

// Add a new person
app.post('/persons', (req, res) => {
    const { Name_, Age, Gender } = req.body;
    pool.query('INSERT INTO person (Name_, Age, Gender) VALUES (?, ?, ?)', [Name_, Age, Gender], (err, results) => {
        if (err) return res.status(500).send(err);
        res.json({ id: results.insertId, Name_, Age, Gender });
    });
});

// Get all sensor data
app.get('/sensor_data', (req, res) => {
    pool.query('SELECT * FROM sensor_data', (err, results) => {
        if (err) return res.status(500).send(err);
        res.json(results);
    });
});

// Add new sensor data
app.post('/sensor_data', (req, res) => {
    const data = req.body; // Assuming the data is sent as a JSON object
    const query = `INSERT INTO sensor_data (${Object.keys(data).join(', ')}) VALUES (${Object.values(data).map(() => '?').join(', ')})`;

    pool.query(query, Object.values(data), (err, results) => {
        if (err) return res.status(500).send(err);
        res.json({ id: results.insertId, ...data });
    });
});

app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});
