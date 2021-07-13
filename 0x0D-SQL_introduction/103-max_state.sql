-- Shows the max temperature of each state
SELECT state, MAX(value) as max_temp
FROM temperatures
GROUP BY STATE
ORDER BY state ASC;
