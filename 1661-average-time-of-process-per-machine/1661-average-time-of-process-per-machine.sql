# Write your MySQL query statement below
with cte as (
select a.machine_id, a.process_id, a.timestamp As start_timestamp, b.timestamp As end_timestamp, 
ROUND(AVG(b.timestamp - a.timestamp), 3) AS processing_time
from Activity a JOIN Activity b ON a.process_id = b.process_id and a.machine_id = b.machine_id and a.activity_type = "start" and b.activity_type = "end"
group by machine_id
    
)

select machine_id, processing_time from cte