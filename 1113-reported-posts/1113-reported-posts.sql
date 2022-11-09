# Write your MySQL query statement below
select a.extra as "report_reason", 
count(distinct post_id) as "report_count" from Actions a
where a.action_date = "2019-07-04" and a.extra is not NULL and a.action = 'report'
group by a.extra