-- This script lists all cities from the state of California in hbtn_0d_usa
-- Get the state_id of California
SELECT
    id
FROM
    states
WHERE
    name = 'California' INTO @california_id;

-- Get the cities linked to that state_id
SELECT
    id,
    name
FROM
    cities
WHERE
    state_id = @california_id
ORDER BY
    id ASC;