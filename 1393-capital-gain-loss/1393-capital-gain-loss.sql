# Write your MySQL query statement below
select stock_name, sum(case when operation = 'Buy' then -price else price end) as "capital_gain_loss"
from Stocks group by stock_name
/*
with cte as (
select stock_name, operation_day, operation,
    sum(price) over(partition by stock_name, operation) as "grouped_company"
    from Stocks
    group by stock_name, operation_day, operation_day
    

), cte_2 as (
    select stock_name, MAX(grouped_company) as "taken_price"
    from cte
    where operation = "Buy"
    group by stock_name
    
), cte_3 as (
    select stock_name, MAX(grouped_company) as "taken_price"
    from cte where operation = "Sell"
    group by stock_name
    
), cte_4 as (
    select c2.stock_name, 
    c2.taken_price as "buy_price", 
    c3.taken_price as "sell_price"
    from cte_2 c2 INNER JOIN cte_3 c3 
    ON c2.stock_name = c3.stock_name
)

select stock_name, 
sell_price - buy_price as "capital_gain_loss"
from cte_4

*/