# Write your MySQL query statement below
SELECT b.player_id, a.event_date, SUM(b.games_played) AS games_played_so_far
FROM Activity a JOIN Activity b ON a.player_id = b.player_id 
AND a.event_date >= b.event_date GROUP BY player_id, event_date