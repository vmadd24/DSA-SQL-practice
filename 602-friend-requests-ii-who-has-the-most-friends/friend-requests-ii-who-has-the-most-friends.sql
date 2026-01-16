# Write your MySQL query statement below

with occurences as (
    select requester_id as combined_column
    from RequestAccepted
    union all
    select accepter_id
    from RequestAccepted
)
    
select
    combined_column as id,
    count(*) as num
from occurences
group by id
order by num desc
limit 1;