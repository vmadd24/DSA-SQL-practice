# Write your MySQL query statement below

with
    join_date_cte as (
        select
            user_id,
            join_date
        from Users
    ),

    numOfOrders2019_cte as (
        select
            buyer_id,
            sum(case
                    when year(order_date) = 2019 then 1
                    else 0
                end) as orders_2019
            from Orders
            group by buyer_id
    )

select
    user_id as buyer_id,
    join_date,
    case
        when orders_2019 is null then 0
        else orders_2019
    end as orders_in_2019
from join_date_cte t1 left join numOfOrders2019_cte t2
    on t1.user_id = t2.buyer_id;