# Write your MySQL query statement below
with cte as (
select log_id, 
    log_id - row_number() over() as "row_difference"
    from Logs

)

select MIN(log_id) as start_id, 
MAX(log_id) as "end_id"
from cte 
group by row_difference 
order by start_id
