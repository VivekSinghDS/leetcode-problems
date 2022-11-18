# Write your MySQL query statement below
select id, 
SUM(IF(month = "Jan", revenue, NULL)) as "Jan_Revenue", 
SUM(IF(month = "Feb", revenue, NULL)) as "Feb_Revenue", 
SUM(IF(month = "Mar", revenue, NULL)) as "Mar_Revenue",
SUM(IF(month = "Apr", revenue, NULL)) as "Apr_Revenue", 
SUM(IF(month = "May", revenue, NULL)) as "May_Revenue", 
SUM(IF(month = "Jun", revenue, NULL)) as "Jun_Revenue",
SUM(IF(month = "Jul", revenue, NULL)) as "Jul_Revenue", 
SUM(IF(month = "Aug", revenue, NULL)) as "Aug_Revenue", 
SUM(IF(month = "Sep", revenue, NULL)) as "Sep_Revenue",
SUM(IF(month = "Oct", revenue, NULL)) as "Oct_Revenue", 
SUM(IF(month = "Nov", revenue, NULL)) as "Nov_Revenue", 
SUM(IF(month = "Dec", revenue, NULL)) as "Dec_Revenue"
from Department 
group by id
