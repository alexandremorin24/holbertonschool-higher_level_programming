-- This script creates the table unique_id_default in the specified database
-- The table has an id that defaults to 1 but remains unique
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL DEFAULT 1,
    name VARCHAR(256),
    PRIMARY KEY (id)
);