# Write your MySQL query statement below

select ROUND(COUNT(DISTINCT b.player_id)/COUNT(DISTINCT a.player_id),2) as fraction from (
select player_id, min(event_date) as event_date from Activity group by player_id) a 
LEFT JOIN Activity b ON 
a.player_id = b.player_id AND a.event_date + 1 = b.event_date

