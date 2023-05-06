# Write your MySQL query statement below

with cte as (
select e.id, e.name, e2.unique_id
    from Employees e LEFT JOIN EmployeeUNI e2
    ON e.id = e2.id

)

select unique_id, name from cte