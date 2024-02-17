-- This script will list all records of a table with rows that have a name

SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
