-- lists all records of the table following;
-- Don’t list rows without a name value
-- should display the score and the name (in this order)
-- Records should be listed by descending score

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
