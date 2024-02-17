-- List all cities of Calfornia that can be found in hbtn_0d_usa
-- States table only contains one record where name == California
-- Results in ascending order by cities.id

SELECT id, name 
FROM cities 
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
