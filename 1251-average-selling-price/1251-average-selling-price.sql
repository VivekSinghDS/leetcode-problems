# Write your MySQL query statement below
with cte as (
select p.product_id, 
    p.price * u.units as "product", 
    u.units 
    from Prices p 
    INNER JOIN UnitsSold u 
    ON p.product_id = u.product_id and u.purchase_date BETWEEN p.start_date AND p.end_date
), cte_2 as (
    select product_id, 
    ROUND(SUM(product) / SUM(units), 2) as "average_price"
    from cte
    group by product_id
    
)

select * from cte_2