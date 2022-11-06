# Write your MySQL query statement below
   
select s.buyer_id from Sales s JOIN Product p ON p.product_id = s.product_id
group by s.buyer_id 
having SUM(p.product_name = "S8") > 0 and SUM(p.product_name = "iPhone") = 0
