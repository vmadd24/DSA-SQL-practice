# Write your MySQL query statement below
with
    grouping_cte as (
        select
            *,
            (id - row_number() over ()) as group_id
        from stadium
        where people >= 100
    ),

    valid_groups_cte as (
        select group_id
        from grouping_cte
        group by group_id
        having count(*) >= 3
    )

select
    id,
    visit_date,
    people
from grouping_cte
where group_id in (
    select *
    from valid_groups_cte
)
order by visit_date