# Write your MySQL query statement below
select IF(id < (select max(id) from seat), IF(id % 2 = 0, id - 1, id + 1), IF(id % 2 = 0, id - 1, id)) AS id, 
student from 
Seat ORDER BY id