# Write your MySQL query statement below
select customer_id from Customer 
where product_key in (select * from Product)
group by customer_id having count(distinct product_key) = (select count(product_key) from Product)

