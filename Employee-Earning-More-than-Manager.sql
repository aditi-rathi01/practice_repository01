CREATE DATABASE office;

USE office;

CREATE TABLE Employee(
 id INT PRIMARY KEY,
 name VARCHAR(10),
 salary INT,
 manager_id INT
);

INSERT INTO Employee
(id, name, salary, manager_id)
VALUES
(1, "Joe", 70000, 3),
(2, "Henery", 80000, 4),
(3, "Sam", 60000, NULL),
(4, "Max", 90000, NULL);

SELECT * FROM Employee;

SELECT e.name 
FROM Employee e
JOIN Employee m
ON e.manager_id = m.id
WHERE e.salary > m.salary;


-- Let's Understand solution step by step


SELECT e.name 
-- Because we only want to show employee names in the result.[e.name = "name of empolyee]

FROM Employee e
-- This means -> "Take the Employee table and call it e". [e = employee data]

JOIN Employee m
-- Take Employee table again and call it m.
   















 



