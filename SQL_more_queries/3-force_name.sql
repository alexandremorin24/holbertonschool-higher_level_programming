-- This script creates the table force_name in the specified database
-- The table will have an id column and a name column that cannot be NULL
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);