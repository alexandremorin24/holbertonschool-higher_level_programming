-- This script lists all records from second_table where name is not NULL or empty, displaying score and name, ordered by highest score first
SELECT score,
    name
FROM second_table
WHERE name IS NOT NULL
    AND name != ''
ORDER BY score DESC;