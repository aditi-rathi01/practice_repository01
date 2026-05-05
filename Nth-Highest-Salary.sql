CREATE DATABASE companies;

USE companies;

CREATE TABLE salaries(
 id INT PRIMARY KEY,
 salary INT
);

INSERT INTO salaries
VALUES
(1, 100),
(2, 44),
(3, 70),
(4, 50),
(5, 89),
(6, 55),
(7, 66),
(8, 70),
(9, 78),
(10, 55);

SELECT * FROM salaries;


SELECT DISTINCT salary
FROM salaries 
ORDER BY salary DESC
LIMIT 1 OFFSET 4;


-- NOTE: 
-- OFFSET: how many rows to skip.
-- LIMIT 1: take only one value.   






















