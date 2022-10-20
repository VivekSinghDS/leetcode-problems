# Write your MySQL query statement below
select name as "Customers" from Customers 
where id not in (
select c.id from Customers c
INNER JOIN Orders o ON c.id = o.customerId 
)
