# Write your MySQL query statement below
with cte as (
    select activity, 
    count(1) over(partition by activity) as "counting"
    from Friends

), cte_2 as (
    select activity, counting from cte
    group by activity
    
    
)

select activity from cte_2 where
counting <> (select min(counting) from cte_2) and counting <> (select max(counting) from cte_2)

    

