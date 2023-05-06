# Write your MySQL query statement below
with cte as (
select v.customer_id, t.transaction_id
    from Visits v LEFT JOIN Transactions t
    ON v.visit_id = t.visit_id
), cte_2 as (
    select * from cte where transaction_id is NULL
)

select customer_id, count(1) as "count_no_trans" from cte_2 group by customer_id 


