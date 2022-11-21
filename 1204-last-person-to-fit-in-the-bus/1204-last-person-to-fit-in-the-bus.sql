# Write your MySQL query statement below
with cte as ( /* template for calculating cumulative sum */
select person_name, weight, 
    SUM(weight) OVER(order by turn) as "counting"
    from Queue

)


select person_name from cte
where counting <= 1000
order by counting DESC LIMIT 1

 
