# Write your MySQL query statement below
with cte as (
select visited_on, SUM(amount) as "total_amount"
    from Customer 
    group by visited_on

), cte_2 as (
select visited_on, 
    SUM(total_amount) OVER(order by visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) AS amount, 
    ROUND(AVG(total_amount) OVER(ORDER BY visited_on ROWS BETWEEN 6 PRECEDING AND CURRENT ROW), 2) as average_amount
    from cte

)

select * from cte_2
WHERE visited_on >= (select visited_on from Customer order by visited_on limit 1) + 6
