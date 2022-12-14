# Write your MySQL query statement below
with cte as 
(
select o.buyer_id, o.order_date from Items i 
    INNER JOIN Orders o ON o.item_id = i.item_id
    where order_date >= "2019-01-01" and order_date <= "2019-12-31"

),cte_2 as (
select buyer_id, u.join_date, count(buyer_id) as "counting" from cte c
INNER JOIN Users u
ON u.user_id = c.buyer_id
group by buyer_id
), cte_3 as (
select u.user_id, u.join_date, c.counting 
from Users u LEFT JOIN cte_2 c ON 
u.user_id = c.buyer_id
    
)

select user_id as "buyer_id", join_date, IF(counting is NULL, 0, counting) as "orders_in_2019"
from cte_3