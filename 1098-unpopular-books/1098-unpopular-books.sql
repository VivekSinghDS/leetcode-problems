# Write your MySQL query statement below
select b.book_id, b.name 
from Books b LEFT JOIN Orders o 
ON b.book_id = o.book_id 
WHERE b.available_from <= date_sub("2019-06-23", INTERVAL 1 month)
group by book_id
having SUM(case when o.dispatch_date >= date_sub("2019-06-23", INTERVAL 1 Year) then o.quantity else 0 end) < 10
