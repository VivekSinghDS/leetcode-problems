select b.book_id, b.name 
from Books b LEFT JOIN Orders o 
ON b.book_id = o.book_id 
WHERE b.available_from <= "2019-05-23"
group by book_id 
having SUM(case when o.dispatch_date >= "2018-06-23" then o.quantity else 0 end) < 10