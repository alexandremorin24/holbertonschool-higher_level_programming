-- This script creates a table called first_table if it does not already exist
CREATE TABLE IF NOT EXISTS users (
    id INT PRIMARY KEY,
    name VARCHAR(255),
    age INT
);