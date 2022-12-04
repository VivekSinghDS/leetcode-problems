# Write your MySQL query statement below
with cte as (
select team_id, count(team_id) as "team_size"
    from Employee 
    group by team_id
), cte_2 as (
select e.employee_id, c.team_size 
    from Employee e INNER JOIN cte c 
    ON e.team_id = c.team_id
)

select * from cte_2