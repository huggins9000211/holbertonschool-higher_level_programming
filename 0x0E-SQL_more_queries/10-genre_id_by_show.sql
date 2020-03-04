-- Show databases
-- Show databases
SELECT tv_shows.title, tv_show_genres.genre_id FROM tv_show_genres, tv_shows 
WHERE tv_shows.id = tv_show_genres.show_id 
GROUP BY tv_shows.title, tv_show_genres.genre_id 
ORDER BY tv_shows.title, tv_show_genres.genre_id ASC;
