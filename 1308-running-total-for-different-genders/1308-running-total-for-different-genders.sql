# Write your MySQL query statement below
with cte as (
select gender, day, 
    SUM(score_points) over(partition by gender order by gender, day) as "total"
    from Scores

)

select * from cte