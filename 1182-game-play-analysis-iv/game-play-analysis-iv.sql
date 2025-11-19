# Write your MySQL query statement below
with first_login as (
    select
        player_id,
        min(event_date) as first_login
    from activity
    group by player_id
)

select round(count(distinct fl.player_id)*(1.0)/(select count(*) from first_login), 2) as fraction
from first_login fl inner join activity a
    on fl.player_id = a.player_id
where DATEDIFF(a.event_date, fl.first_login) = 1