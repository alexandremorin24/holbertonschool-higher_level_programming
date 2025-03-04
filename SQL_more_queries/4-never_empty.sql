-- This script creates the table id_not_null in the specified database
-- The table will have an id column with a default value of 1 and a name column
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256)
);