SELECT d.name as "Department", e.name as "Employee", e.salary as "Salary" from (
SELECT departmentId, name, salary, 
dense_rank() over(partition by departmentId order by salary desc) as r
from Employee) e INNER JOIN Department d ON d.id = e.departmentId
WHERE r <= 3