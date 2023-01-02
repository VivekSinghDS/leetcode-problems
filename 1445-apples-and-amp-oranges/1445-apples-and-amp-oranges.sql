# Write your MySQL query statement below
with cte as (
select sale_date, 
    fruit, sold_num as "apple_quantity"
    from Sales 
    where fruit = "apples"
    group by sale_date, fruit

), cte_2 as (
    select sale_date, 
    fruit, sold_num as "orange_quantity"
    from Sales
    where fruit = "oranges"
    group by sale_date, fruit
    

)

select c.sale_date, 
c.apple_quantity - c2.orange_quantity as "diff"
from cte c, cte_2 c2
where c.sale_date = c2.sale_date
order by sale_date
