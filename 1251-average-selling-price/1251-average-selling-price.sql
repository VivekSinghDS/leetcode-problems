# Write your MySQL query statement below
with cte as (
    select p.product_id, SUM(u.units) as "units", SUM(p.price * u.units) as "cost"
    from Prices p INNER JOIN UnitsSold u
    ON p.product_id = u.product_id AND u.purchase_date BETWEEN p.start_date AND p.end_date
    group by product_id
)

select product_id, ROUND(cost/units, 2) as average_price
from cte