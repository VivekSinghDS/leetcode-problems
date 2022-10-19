# Write your MySQL query statement below
select e.name as "Employee" from Employee e 
INNER JOIN Employee e2 
WHERE e.managerId = e2.id
AND e.salary > e2.salary