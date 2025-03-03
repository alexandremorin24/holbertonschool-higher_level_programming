-- This script updates Bob's score to 10 without using his id, only using the name field
UPDATE second_table
SET score = 10
WHERE name = 'Bob';