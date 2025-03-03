-- This script lists the number of records for each score in second_table, displaying score and count as 'number', ordered by highest count first
SELECT score,
    COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY number DESC;