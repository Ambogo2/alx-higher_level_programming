-- a script that lists all shows from hbtn_0d_tvshows_rate by their rating.

SELECT tv_shows.title , sum(tv_shows_ratings.rate) AS rating_sum
FROM  tv_shows
LEFT JOIN tv_shows_ratings
ON  tv_shows.show_id = tv_show_ratings.id
GROUP BY tv_shows.title
ORDER BY rating sum DESC;
