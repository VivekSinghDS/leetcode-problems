# Write your MySQL query statement below
select e.name from (
    select c.id, c.name from Candidate c INNER JOIN 
    VOTE v ON c.id = v.candidateId 
) e group by e.name ORDER BY count(*) desc LIMIT 1
