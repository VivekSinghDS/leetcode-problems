# Write your MySQL query statement below
with cte as (
select *, 
    dense_rank() over(partition by product_id order by change_date DESC) as "ranking"
    from Products
    where change_date <= "2019-08-16"
    

    
), cte_2 as(

select * from cte where ranking = 1
)

select p.product_id , IF(c.new_price is not NULL, c.new_price, 10) as "price"
from Products p LEFT JOIN cte_2 c
ON p.product_id = c.product_id
group by p.product_id


