
/* The different lines are used to  select (a) column(s)
   from a table */
SELECT first_name FROM Person;
SELECT first_name, age FROM Person;
SELECT DISTINCT color FROM EyesColor;

/* The result here is sorted by age in ascending order */
SELECT first_name, last_name, age FROM Person
ORDER BY age ASC;
