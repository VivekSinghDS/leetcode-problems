# Write your MySQL query statement below
with cte as (
select seller_id, SUM(price) as "price"
from Sales group by seller_id
), cte_2 as (
    select seller_id, 
        dense_rank() over(order by price desc) as "ranker" from cte
    )

select seller_id from cte_2 where ranker = 1