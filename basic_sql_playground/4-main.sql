/* Changes Jon Snow's eye color to Brown */
UPDATE EyesColor
SET color = 'Brown'
WHERE person_id = (
    SELECT id FROM Person
    WHERE first_name = 'Jon' AND last_name = 'Snow'
);

/* Changes Arya Stark's eye color to Green */
UPDATE EyesColor
SET color = 'Green'
WHERE person_id = (
    SELECT id FROM Person
    WHERE first_name = 'Arya' AND last_name = 'Stark'
);

/* Creates a new table*/
CREATE TABLE TVShow (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    name char(128) NOT NULL
);

/* Creates a new table*/
CREATE TABLE TVShowPerson (
    tvshow_id INTEGER NOT NULL,
    person_id INTEGER NOT NULL,
    FOREIGN KEY(tvshow_id) REFERENCES TVShow(id)
    FOREIGN KEY(person_id) REFERENCES Person(id)
);

/* Creates new records in the TVShow table */
INSERT INTO TVShow (name)
VALUES ('Homeland'), ('The big bang theory'),
('Game of Thrones'), ('Breaking bad');

/* Uses nested SELECTS to create new records in TVShowPerson */
INSERT INTO TVShowPerson (tvshow_id, person_id) VALUES
(
    (SELECT id FROM TVShow WHERE name = 'Breaking bad'),
    (SELECT id FROM Person WHERE first_name = 'Walter Junior' AND last_name = 'White')
),
(
    (SELECT id FROM TVShow WHERE name = 'Game of Thrones'),
    (SELECT id FROM Person WHERE first_name = 'Jaime' AND last_name = 'Lannister')
),
(
    (SELECT id FROM TVShow WHERE name = 'The big bang theory'),
    (SELECT id FROM Person WHERE first_name = 'Sheldon' AND last_name = 'Cooper')

),
(
    (SELECT id FROM TVShow WHERE name = 'Game of Thrones'),
    (SELECT id FROM Person WHERE first_name = 'Tyrion' AND last_name = 'Lannister')

),
(
    (SELECT id FROM TVShow WHERE name = 'Game of Thrones'),
    (SELECT id FROM Person WHERE first_name = 'Jon' AND last_name = 'Snow')

),
(
    (SELECT id FROM TVShow WHERE name = 'Game of Thrones'),
    (SELECT id FROM Person WHERE first_name = 'Arya' AND last_name = 'Stark')

);

/* Prints all columns of the given table */
SELECT * FROM Person;
SELECT * FROM EyesColor;
SELECT * FROM TVShow;
SELECT * FROM TVShowPerson;
