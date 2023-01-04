# Write your MySQL query statement below
with cte as (
select content_id, title from 
    Content 
    where Kids_content = "Y" and content_type = "Movies"

), cte_2 as (
    select content_id 
    from TVProgram 
    where EXTRACT(MONTH from program_date) = "6" AND EXTRACT(YEAR from program_date) = "2020"

), cte_3 as (
    select distinct c.title
    from cte_2 c2 INNER JOIN cte c 
    ON c2.content_id = c.content_id

)


select * from cte_3