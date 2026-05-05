CREATE DATABASE Intro;

USE Intro;

CREATE TABLE person_table(
 person_id INT PRIMARY KEY,
 last_name VARCHAR(10),
 first_name VARCHAR(10)
);

INSERT INTO person_table
VALUES
(1, "Wang", "Allen"),
(2, "Alice", "Bob");

SELECT * FROM person_table;

CREATE TABLE address_table(
 address_id INT PRIMARY KEY,
 person_id INT,
 city VARCHAR(15),
 state VARCHAR(15)
);

INSERT INTO address_table
VALUES
(1, 2, "New York City", "New York"),
(2, 3, "Leetcode", "California");

SELECT * FROM address_table;

SELECT first_name as firstname , last_name as lastname, city, state
FROM person_table
LEFT JOIN address_table
ON person_table.person_id = address_table.person_id;






