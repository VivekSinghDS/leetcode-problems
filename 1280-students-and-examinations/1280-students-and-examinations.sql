# Write your MySQL query statement below
with cte as (
    select * from Students JOIN Subjects
), cte_2 as (
    select student_id, subject_name, 
    count(*) as "attended_count" from Examinations 
    group by student_id, subject_name
), cte_3 as (
    select c.student_id, c.student_name, c.subject_name, IF(c2.attended_count is NULL, 0, c2.attended_count) as "attended_exams"
    from cte c LEFT JOIN cte_2 c2 ON c.student_id = c2.student_id AND c.subject_name = c2.subject_name
    order by student_id, subject_name

)

select * from cte_3