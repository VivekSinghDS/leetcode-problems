# Write your MySQL query statement below
with cte as (
select a.id as "p1", b.id as "p2", 
    abs(a.x_value - b.x_value) * abs(a.y_value - b.y_value) as "area" from 
    Points a JOIN Points b 
    ON a.id < b.id and a.x_value != b.x_value and a.y_value != b.y_value 
)

select * from cte
where area > 0
order by area DESC, p1 ASC, p2 ASC