# Write your MySQL query statement below
with cte as (
select e.*, 
    CASE 
        when e.operator = ">" AND v1.value > v2.value then "true"
        when e.operator = "<" AND v1.value < v2.value then "true"
        when e.operator = "=" AND v1.value = v2.value then "true"
    else "false"
    END as "value"
    
    
    from Expressions e 
    LEFT JOIN Variables v1 
    on v1.name = e.left_operand
    LEFT JOIN Variables v2 
    ON v2.name = e.right_operand
    

)

select * from cte