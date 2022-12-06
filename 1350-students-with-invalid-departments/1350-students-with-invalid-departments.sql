# Write your MySQL query statement below
with cte as (
    select s.id, s.name, d.name as "dept_name"
    from Students s LEFT JOIN Departments d
    ON s.department_id = d.id

)

select id, name from cte
where dept_name is NULL
