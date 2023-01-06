# Write your MySQL query statement below
with cte as (
select quantity, 
    product_id, 
    customer_id, 
    order_date from 
    Orders 
    where EXTRACT(year from order_date) = "2020" AND 
        extract(month from order_date) = "6" or extract(month from order_date) = "7"

), cte_2 as (
select c.quantity * p.price as "expenditure", 
    c.product_id, 
    c.customer_id,
    c.order_date
    
    from cte c
    INNER JOIN Product p 
    ON p.product_id = c.product_id

), cte_3 as (
    select product_id, 
    customer_id, order_date, SUM(expenditure) as "total"
    from cte_2
    group by customer_id, EXTRACT(month from order_date)
    having total >= 100


), cte_4 as (
select customer_id from cte_3
group by customer_id 
having count(*) = 2
    
)
select c.customer_id, name from Customers c INNER JOIN cte_4 c4 ON c4.customer_id = c.customer_id

