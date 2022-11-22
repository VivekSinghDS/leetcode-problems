# Write your MySQL query statement below
select team_id, team_name, 

SUM(IF(team_id = host_team AND host_goals > guest_goals, 3, 0)) + 
SUM(IF(team_id = guest_team AND guest_goals > host_goals, 3, 0)) + 
SUM(IF(team_id = host_team and host_goals = guest_goals, 1, 0)) + 
SUM(IF(team_id = guest_team AND guest_goals = host_goals, 1, 0)) as "num_points"

from 
Teams t LEFT JOIN 
Matches m ON 
t.team_id = m.host_team or t.team_id = guest_team
group by team_id
order by num_points DESC, team_id

