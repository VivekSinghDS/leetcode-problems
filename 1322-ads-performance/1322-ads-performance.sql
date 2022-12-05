# Write your MySQL query statement below
with cte as (
    select ad_id, 
    count(1) over(partition by ad_id) as "counting"
    from Ads 
    where action = "Clicked" or action = "Viewed"
    
), cte_2 as (
    select ad_id, 
    count(1) over(partition by ad_id) as "clicks"
    from Ads
    where action = "Clicked"
    
), cte_3 as (
    select c.ad_id, 
    ROUND((c2.clicks / c.counting)*100, 2) as "ctr"
    from cte c INNER JOIN cte_2 c2
    ON c.ad_id = c2.ad_id
    
), cte_4 as (
    select distinct ad_id from Ads 
), cte_5 as (
    select c4.ad_id, c3.ctr 
    from cte_4 c4 LEFT JOIN cte_3 c3
    ON c4.ad_id = c3.ad_id
)

select ad_id, 
IF(ctr is NULL, 0.00, ctr) as "ctr"
from cte_5
group by ad_id
order by ctr desc, ad_id
