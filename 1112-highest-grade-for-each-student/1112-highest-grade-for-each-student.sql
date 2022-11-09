# Write your MySQL query statement below
with cte as (
select student_id, course_id, grade, 
rank() OVER(partition by student_id order by grade desc, course_id ASC) as "ranking"
from Enrollments
group by student_id, course_id
    
)

select student_id, course_id, grade from cte where ranking = 1






