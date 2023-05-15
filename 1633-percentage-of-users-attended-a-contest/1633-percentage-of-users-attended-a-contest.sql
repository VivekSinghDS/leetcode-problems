# Write your MySQL query statement below
with cte as (
    select contest_id, ROUND(COUNT(user_id)/(select count(user_id) from Users) * 100, 2) as "percentage"
    from Register 
    group by contest_id
    order by percentage desc, contest_id asc
)

select * from cte