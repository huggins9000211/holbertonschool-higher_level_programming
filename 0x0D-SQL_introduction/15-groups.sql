-- Show databases
-- Show databases
SELECT DISTINCT(score), COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
