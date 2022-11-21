# Write your MySQL query statement below
select date_format(trans_date, "%Y-%m") as month, 
country, 
count(*) as "trans_count", 
SUM(CASE when state = 'approved' then 1 else 0 end) as "approved_count", 
SUM(amount) as "trans_total_amount",
SUM(CASE when state = 'approved' then amount else 0 end) as "approved_total_amount"
from Transactions
group by country, month