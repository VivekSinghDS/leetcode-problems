# Write your MySQL query statement below

with cte as (
select e2.unique_id, e.name 
    from EmployeeUNI e2 RIGHT JOIN Employees e 
    ON e.id = e2.id

)
select * from cte