-- a script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter

SELECT tv_genres.name
FROM tv_genres
WHERE tv_genres.id  IN(
    SELECT tv_shows_genres.genre_id
    FROM tv_shows 
    JOIN tv_shows_genres ON tv_shows.id = tv_show_genres.show_id
    WHERE tv_shows.title = 'Dexter'
)
ORDER BY tv_genres.name;
