# Write your MySQL query statement below
with cte as (
    select managerId, count(*) as "counting"
    from Employee 
    group by managerId 
    having counting >= 5
), cte_2 as (
    select e.name from Employee e INNER JOIN cte c ON c.managerId = e.id
    
)

select * from cte_2