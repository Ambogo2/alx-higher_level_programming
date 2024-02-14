-- a script that lists all genres in the database hbtn_0d_tvshows_rate by their rating

SELECT name, sum(rate) AS rating_sum
FROM  tv_genres
ORDER BY rating_sum DESC;
