# Write your MySQL query statement below
with cte as (
select product_id, order_date, unit from 
    Orders 
    where EXTRACT(MONTH from order_date) = 2 and EXTRACT(YEAR from order_date) = 2020
), cte_2 as (
    select p.product_id, p.product_name,
    SUM(o.unit) over(partition by o.product_id) as "unit"
    from Products p INNER JOIN cte o ON p.product_id = o.product_id

)

select product_name, unit from cte_2 
where unit >= 100 
group by product_id

