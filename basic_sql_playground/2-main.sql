/* A record is added into the Person table */
INSERT INTO Person (first_name, last_name, age)
VALUES ('Jon', 'Snow', 26);

/* Another record is added to the Person table */
INSERT INTO Person (first_name, last_name, age)
VALUES ('Arya', 'Stark', 12);

/* All the columns from Person are printed
   and sorted by last name in ascending order */
SELECT * FROM Person
ORDER BY last_name ASC;
