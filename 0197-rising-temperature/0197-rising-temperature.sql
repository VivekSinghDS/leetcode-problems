# Write your MySQL query statement below
with cte as (
    select id, 
    lag(temperature) over(order by recordDate) as "previous_temperature",
    lag(recordDate) over(order by recordDate) as "previous_date", temperature, recordDate
    from  Weather
)

select id from cte
where temperature - previous_temperature > 0 and DATEDIFF(recordDate, previous_date) = 1