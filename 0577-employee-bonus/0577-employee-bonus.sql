# Write your MySQL query statement below
select ex.name, ex.bonus from (select e.name, b.bonus from 
Employee e LEFT JOIN Bonus b 
ON e.empId = b.empId) ex
where ex.bonus is NULL or ex.bonus < 1000