# Write your MySQL query statement below
# select * from Employee e JOIN Employee e1
# WHERE e.id = e1.managerId
select name from Employee e
JOIN (
select managerId from Employee 
    group by managerId having COUNT(managerId) >= 5
) e2 ON e.id = e2.ManagerId