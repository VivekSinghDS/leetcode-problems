# Write your MySQL query statement below
with cte as (
select country_id, weather_state, day
    from Weather where
    EXTRACT(YEAR from day) = "2019" AND 
    EXTRACT(MONTH from day) = "11" 
), cte_2 as (
    select country_id, AVG(weather_state) as "average_weather"
    from cte 
    group by country_id
), cte_3 as (
    select c2.average_weather, c.country_name 
    from cte_2 c2 INNER JOIN Countries c 
    ON c.country_id = c2.country_id
)

select country_name, 
(
CASE
when (average_weather <= 15) THEN "Cold"
when (average_weather >= 25) THEN "Hot"
else "Warm"
END
    ) as weather_type
from cte_3

