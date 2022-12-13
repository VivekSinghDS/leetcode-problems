# Write your MySQL query statement below
select c.customer_id, 
c.customer_name 
from Customers c 
INNER JOIN Orders o 
ON o.customer_id = c.customer_id 
group by customer_id
having sum(o.product_name = "A") > 0 and sum(o.product_name = "B") > 0 and sum(o.product_name = "C") = 0


