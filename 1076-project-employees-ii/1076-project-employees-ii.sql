# Write your MySQL query statement below
# select p.project_id from 
# (select project_id, count(employee_id) as "num_of_emp" from Project 
# group by project_id ) p
# where p.num_of_emp = (select max(x.num_of_emp) from 
#                      (select project_id, count(employee_id) as "num_of_emp" from Project 
#                         group by project_id ) x)

with cte as 
(select project_id, count(employee_id) as "num_of_emp" from Project 
group by project_id)

select project_id from 
cte 
where num_of_emp = (select max(num_of_emp) from cte)