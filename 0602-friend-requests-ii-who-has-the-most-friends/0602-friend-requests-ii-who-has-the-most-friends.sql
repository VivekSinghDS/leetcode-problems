# Write your MySQL query statement below
with cte as (
    select requester_id as "id", accepter_id
    from RequestAccepted 
    
    UNION 
    
    select accepter_id as "id", requester_id
    from RequestAccepted 
    

)

select id, count(DISTINCT accepter_id) as "num" from cte
group by id
order by num 
desc
limit 1