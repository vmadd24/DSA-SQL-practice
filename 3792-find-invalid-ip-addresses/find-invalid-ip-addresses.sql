# Write your MySQL query statement below

select
    ip,
    count(*) as invalid_count
from logs
where ip not regexp '^(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])$'
group by ip
order by invalid_count desc, ip desc