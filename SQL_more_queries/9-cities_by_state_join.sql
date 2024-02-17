-- Show all cities contained in the database, with their respective state.

SELECT cities.id, cities.name, states.name 
FROM cities, states 
WHERE cities.state_id = states.id
ORDER BY cities.id;