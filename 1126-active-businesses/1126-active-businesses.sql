# Write your MySQL query statement below
with cte as 
(
select avg(occurences) as "average", event_type from 
    Events group by event_type

)

select e.business_id from Events e
JOIN cte c ON c.event_type = e.event_type
AND e.occurences > c.average
group by business_id 
having count(*) > 1
    
