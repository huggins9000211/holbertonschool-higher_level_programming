-- Show databases
-- Show databases
SELECT id, name FROM cities 
WHERE state_id = (
    SELECT MAX(id) FROM states WHERE name = California
)ORDER BY id ASC;
