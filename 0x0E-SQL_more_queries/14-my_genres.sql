-- Show databases
-- Show databases
SELECT tv_shows.title FROM tv_shows 
JOIN tv_show_genres ON tv_showss.id = tv_show_genres.show_id 
JOIN tv_geners ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_geners.name = 'Comedy'
ORDER BY tv_shows.title;
