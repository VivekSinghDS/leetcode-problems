# Write your MySQL query statement below
with cte as (
    select count(*) as "total", 
    class 
    from Courses 
    group by class
)

select class from cte
where total >= 5