# Write your MySQL query statement below
with cte as (
select q1.person_id, q1.person_name, q1.turn, SUM(q2.weight) as "cumulative"
    from Queue q1
    INNER JOIN Queue q2 ON q1.turn >= q2.turn
    group by q1.turn, q1.weight
    HAVING cumulative <= 1000
    order by q1.turn  
    

)

select person_name from cte
order by cumulative desc 
LIMIT 1
 
