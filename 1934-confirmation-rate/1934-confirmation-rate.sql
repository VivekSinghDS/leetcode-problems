# Write your MySQL query statement below
with cte as (
select user_id, ROUND(SUM(action = "confirmed")/COUNT(*), 2) as "percentage"
from Confirmations 
group by user_id
), cte_2 as (
    select s.user_id, IF(c.percentage is NULL, 0.00, c.percentage) as "confirmation_rate"
    from Signups s LEFT JOIN cte c 
    ON s.user_id = c.user_id

)

select * from cte_2