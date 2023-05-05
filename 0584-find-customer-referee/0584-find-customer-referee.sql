# Write your MySQL query statement below
with cte as (
    select name from Customer
    where referee_id != 2 or referee_id is NULL
)

select * from cte
