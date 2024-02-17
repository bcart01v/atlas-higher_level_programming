-- This script will group stuff. 

SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score
ORDER BY score DESC;
