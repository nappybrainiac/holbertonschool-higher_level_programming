\! echo "\nList of all TVShows by all Genres ordered by genre name (A-Z)? (if a genre has 0 TVShow, please display NULL)"
SELECT Genre.name AS 'Genre name',
     CASE TVShow.name
        WHEN TVShow.name = '' THEN
      END AS 'TVShow name'
FROM TVShow, Genre, TVShowGenre
WHERE TVShow.id = TVShowGenre.tvshow_id  or TVShowGenre.genre_id = Genre.id
ORDER BY Genre.name ASC;


\! echo "\nName of the pilot (first episode of the first season) of each TVShow ordered by TVShow name (A-Z)?"


\! echo "\nList of all Genres by all TVShows ordered by TVShow name (A-Z)? (if a genre has 0 TVShow, please display NULL as TVShow name)"
