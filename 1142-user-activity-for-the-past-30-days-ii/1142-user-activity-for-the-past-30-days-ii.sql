# Write your MySQL query statement below
with cte as 
(
    select user_id, count(distinct session_id) as "counting" from Activity
    where activity_date between date_sub('2019-07-27', interval 29 day) and '2019-07-27'
    group by user_id
)

select IF(ROUND(avg(counting), 2) is not NULL, ROUND(avg(counting), 2), 0.00) as "average_sessions_per_user" from cte