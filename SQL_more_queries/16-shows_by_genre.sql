-- Show all shows, all genres linked to that show.

SELECT tv_shows.title, tv_genres.Name AS name
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.ID = tv_show_genres.show_id
LEFT JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.ID
ORDER BY tv_shows.title ASC, tv_genres.Name ASC;
