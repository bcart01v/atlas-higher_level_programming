-- List all shows contained in hbtn_0d_tvshows that have at least 1 genre linked
-- Display tv_shows.title, tv_show_genres.genre_id
-- 1 select. 

SELECT tv_shows.title, tv_show_genres.genre_id
FROM hbtn_0d_tv_shows
JOIN tv_show_genres ON tv_shows.id = tv_show_genres.tv_show_id
WHERE tv_shows_genres.genre_id IS NOT NULL
ORDER BY tv_shows.title, tv_show_genres.genre_id;