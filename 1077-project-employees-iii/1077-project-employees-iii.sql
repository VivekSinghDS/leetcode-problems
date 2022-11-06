# Write your MySQL query statement below
with cte as (
select p.project_id, e.employee_id, 
dense_rank() over(partition by p.project_id order by e.experience_years desc) as "most_exp_emp" from 
Employee e INNER JOIN Project p ON 
e.employee_id = p.employee_id


)


/*select * from 
Employee where experience_years = (select maximum_experience from cte)*/

select project_id, employee_id from cte where most_exp_emp = 1