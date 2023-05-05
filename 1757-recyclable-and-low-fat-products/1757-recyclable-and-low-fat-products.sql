# Write your MySQL query statement below
with cte as (
    select product_id from Products 
    where low_fats = "Y" and recyclable = "Y"
    
)

select * from cte
