# Write your MySQL query statement below
select a.employee_id from Employees a 
JOIN Employees b JOIN Employees c ON
a.manager_id = b.employee_id and 
b.manager_id = c.employee_id
where c.manager_id = 1 and a.employee_id <> 1