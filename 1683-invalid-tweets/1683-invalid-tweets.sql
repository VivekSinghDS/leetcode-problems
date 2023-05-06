# Write your MySQL query statement below
with cte as (
select tweet_id from Tweets 
    where CHAR_LENGTH(content) > 15

)

select * from cte