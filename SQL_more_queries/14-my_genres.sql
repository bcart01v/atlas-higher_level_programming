-- List all genres where Dexter is considered.

SELECT tv_genres.Name AS name
FROM tv_shows
JOIN tv_show_genres ON tv_shows.ID = tv_show_genres.show_id
JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.ID
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.Name;