# Write your MySQL query statement below
with cte as 
(
select viewer_id, view_date, COUNT(distinct article_id) as "counting"
    from Views 
    group by viewer_id, view_date
    Having counting > 1

)

select distinct viewer_id as "id" from cte