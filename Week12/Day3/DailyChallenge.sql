-- TASK: Actors

--  Instructions
--      In this exercise we will be using the actors table from todays lesson.
--      1. Count how many actors are in the table.
--      2. Try to add a new actor with some blank fields. What do you think the outcome will be ?

CREATE TABLE actors(
 actor_id SERIAL PRIMARY KEY,
 first_name VARCHAR (50) NOT NULL,
 last_name VARCHAR (100) NOT NULL,
 age DATE NOT NULL,
 number_oscars SMALLINT NOT NULL
);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Matt','Damon','08/10/1970', 5);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('George','Clooney','06/05/1961', 2);

INSERT INTO actors (first_name, last_name, age, number_oscars)
VALUES('Gal','Gadot','03/04/1985', 0), ('Bradley','Cooper','05/01/1965', 0), ('Brad','Pitt','18/12/1963', 1),
       ('Scarlett','Johansson','22/11/1984', 0), ('Leonardo','DiCaprio','11/11/1974', 1);

SELECT * FROM actors;

SELECT COUNT(*) FROM actors;


-- INSERT INTO actors (first_name, last_name, age, number_oscars)
-- VALUES('George','Clooney','06/05/1961', );

--  Error occurred: <expression> expected, got ')'