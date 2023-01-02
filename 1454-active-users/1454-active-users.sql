# Write your MySQL query statement below
with temp0 AS
(SELECT  id,
            login_date,
            dense_rank() OVER(PARTITION BY id ORDER BY login_date) as row_num
    FROM Logins), 
    
temp1 as (
select id, login_date, row_num,
        DATE_ADD(login_date, INTERVAL -row_num DAY) as Groupings
    from temp0
), 

cte_3 as (
SELECT  id,
         MIN(login_date) as startDate,
         MAX(login_date) as EndDate,
         row_num,
         Groupings, 
         count(id),
        datediff(MAX(login_date), MIN(login_date)) as duration
 FROM temp1
    group by id, Groupings
    having datediff(EndDate, startDate) >= 4
    order by id, startDate
    

)
    
    
select distinct a.id, a.name from cte_3 c 
INNER JOIN Accounts a 
ON a.id = c.id
order by a.id