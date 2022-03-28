-- CREATE TABLE FirstTab (
--      id integer,
--      name VARCHAR(10)
-- );
--
-- INSERT INTO FirstTab VALUES
-- (5,'Pawan'),
-- (6,'Sharlee'),
-- (7,'Krish'),
-- (NULL,'Avtaar');
--
-- SELECT * FROM FirstTab;
--
-- CREATE TABLE SecondTab (
--     id integer
-- );
--
-- INSERT INTO SecondTab VALUES
-- (5),
-- (NULL);
--
--
-- SELECT * FROM SecondTab

SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NULL);
-- Number of rows in first table that their id isn't equal to NULL (EVERYTHING that equalized to NULL is NULL): 0

SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id = 5);
-- Number of rows in first table that their id isn't equal to 5: 2

SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab);
-- Number of rows in first table that their id isn't equal to 5 or NULL (EVERYTHING that equalized to NULL is NULL): 0

SELECT COUNT(*) FROM FirstTab AS ft WHERE ft.id NOT IN (SELECT id FROM SecondTab WHERE id IS NOT NULL)
-- Number of rows in first table that their id isn't equal to anything that isn't NULL (5): 2