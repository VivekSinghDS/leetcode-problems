# Write your MySQL query statement below
select s.product_id, p.product_name from Sales s 
INNER JOIN Product p ON s.product_id = p.product_id
group by s.product_id HAVING
MIN(s.sale_date) >= "2019-01-01" and MAX(s.sale_date) <= "2019-03-31"