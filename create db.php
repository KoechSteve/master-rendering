<?php
// Connect to the SQLite database
$db = new SQLite3('master_rendering.db');

// Create a Clients table
$db->exec('CREATE TABLE IF NOT EXISTS clients (id INTEGER PRIMARY KEY, name TEXT)');

// Create a Renderers table
$db->exec('CREATE TABLE IF NOT EXISTS renderers (id INTEGER PRIMARY KEY, name TEXT, days_worked INTEGER, pay_per_day REAL)');
?>
