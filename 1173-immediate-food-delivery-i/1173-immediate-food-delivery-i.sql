# Write your MySQL query statement below
with cte as (
select count(delivery_id) as "c1"
    from Delivery 
    where order_date = customer_pref_delivery_date
), 

cte_2 as (
    
select count(distinct delivery_id) as "c2" from Delivery
    
)

select ROUND((c1/c2)*100, 2) as "immediate_percentage" from cte, cte_2 
