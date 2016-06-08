/* Jon Snow's age is updated to 27*/
UPDATE Person
SET age = 27
WHERE last_name = 'Snow';

/* Someone with junior in their name
   has their age updated to 18 */
UPDATE Person
SET age = 18
WHERE first_name = '%junior%';

/* Walter White is deleted from the table
   EyesColor */
DELETE FROM EyesColor
WHERE person_id = (
    SELECT id FROM Person
    WHERE first_name ='Walter'
    AND last_name = 'White');

/* Walter white is deleted from the table
   Person */
DELETE FROM Person
WHERE first_name = 'Walter' AND last_name = 'White';

/* All the columns in the table Person are
   displayed and sorted by first name in
   ascending order*/
SELECT * FROM Person
ORDER BY first_name ASC;
