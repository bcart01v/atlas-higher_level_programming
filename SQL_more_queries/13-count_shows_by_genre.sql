-- Count the number of TV Shows liked by genres. Basically.

SELECT tv_genres.Name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_show_genres ON tv_genres.ID = tv_show_genres.genre_id
GROUP BY tv_genres.ID
HAVING COUNT(tv_show_genres.show_id) > 0
ORDER BY number_of_shows DESC;
