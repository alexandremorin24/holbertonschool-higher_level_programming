-- This script lists all TV shows that do not have any genre linked from hbtn_0d_tvshows
SELECT
    tv_shows.title,
    tv_show_genres.genre_id
FROM
    tv_shows
    LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE
    tv_show_genres.genre_id IS NULL
ORDER BY
    tv_shows.title ASC,
    tv_show_genres.genre_id ASC;