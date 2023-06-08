# Write your MySQL query statement below
with cte as (
    select e.employee_id, e.name, COUNT(e2.employee_id) as 'reports_count', ROUND(AVG(e2.age), 0) as "average_age"
    from Employees e INNER JOIN Employees e2 
    ON e.employee_id = e2.reports_to
    group by employee_id
    order by employee_id

)

select * from cte
