-- lists all the cities of California that can be found in the database
SELECT * FROM cities
WHERE state_id = (SELECT id FROM states WHERE  name = 'Californi')
ORDER BY id  ASC;