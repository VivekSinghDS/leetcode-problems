# Write your MySQL query statement below
with cte as (
select q.id, q.year, n.npv 
    from NPV n RIGHT JOIN Queries q 
    ON q.id = n.id and q.year = n.year

)

select id, year, 
IF(npv is null, 0, npv) as "npv"
from cte