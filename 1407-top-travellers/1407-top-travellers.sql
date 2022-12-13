# Write your MySQL query statement below
with cte as (
select u.id, u.name,
    IF(sum(r.distance) is null, 0, sum(r.distance)) as "travelled_distance"
    from Users u LEFT JOIN Rides r 
    ON u.id = r.user_id
    group by u.id
    order by travelled_distance desc, name

)
select name, travelled_distance from cte