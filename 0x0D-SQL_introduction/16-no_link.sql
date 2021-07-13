-- "Who are you?. The man who killed Gus Fring, now, say my name. You are, Heisenberg"
SELECT score, name 
FROM second_table 
WHERE name IS NOT NULL 
ORDER BY score DESC;
