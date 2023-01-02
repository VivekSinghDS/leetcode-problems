# Write your MySQL query statement below
with cte as (
select * from (
    select company_id, 
        max(salary) over(partition by company_id order by salary desc) as "maximum_salary_per_company"
        from Salaries
            ) e
    
    group by company_id 
), cte_2 as (
select s.company_id, s.employee_id, s.employee_name, 
    s.salary, c.maximum_salary_per_company
    from Salaries s
    INNER JOIN cte c
    ON c.company_id = s.company_id

), cte_3 as (
select company_id, employee_id, employee_name,
    (
        CASE
        WHEN maximum_salary_per_company < 1000 then salary
        when maximum_salary_per_company >= 1000 && maximum_salary_per_company <= 10000 then ROUND(salary*0.76)
        else ROUND(salary*0.51)
        end
    ) as salary
    from cte_2
)

select * from cte_3
