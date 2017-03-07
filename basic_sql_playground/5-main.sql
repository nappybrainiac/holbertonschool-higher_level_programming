/* Returns a table of all the characters in Game of Thrones
   and sorts them in ascending order (a-z) */
SELECT DISTINCT last_name FROM Person
    JOIN TVShowPerson ON TVShowPerson.person_id = Person.id,
         TVShow ON TVShowPerson.tvshow_id = TVShow.id
    WHERE name = "Game of Thrones"
    ORDER BY last_name ASC;

/* Returns a table from 3 different tables by joining
   Person TVShow TVShowPerson and EyesColor. */
SELECT Person.id, first_name, last_name, age, color, name FROM Person
       JOIN TVShowPerson ON TVShowPerson.person_id = Person.id,
            TVShow ON TVShow.id = TVShowPerson.tvshow_id,
	        EyesColor ON EyesColor.person_id = Person.id;

/* Returns the sum of all the ages */
SELECT SUM(age) FROM Person;
