# Write your MySQL query statement below
select id, company, salary from (
select id, company, salary, 
ROW_NUMBER() OVER(partition by company order by salary) as r_number, 
COUNT(id) OVER(partition by company) as n
from Employee) e where 
r_number BETWEEN (n / 2) AND (n / 2) + 1

