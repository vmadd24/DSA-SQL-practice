# Write your MySQL query statement below

with threeconsec as (

    select
        num,
        id,
        LAG(id, 2, -5) over (
            partition by num
            order by id
        ) as second_last_id
    from Logs
)

select distinct
    num as  ConsecutiveNums
from threeconsec
where id - second_last_id = 2;