-- This script creates the 'cities' table with an auto-increment ID, a name, and a foreign key 'state_id' referencing 'states(id)' with ON DELETE CASCADE.
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL,
    state_id INT NOT NULL,
    FOREIGN KEY (state_id) REFERENCES states(id) ON DELETE CASCADE
);