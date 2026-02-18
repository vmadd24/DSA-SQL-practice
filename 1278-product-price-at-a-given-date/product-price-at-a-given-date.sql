# Write your MySQL query statement below

with product_price_cte as (
    select
        product_id,
        new_price as price,
        row_number() over (
            partition by product_id
            order by change_date desc
        ) as date_rank
        from Products
        where change_date <= '2019-08-16'
)

select
    product_id,
    price
from product_price_cte
where date_rank = 1

union all

select
    product_id,
    10 as price
from Products
group by product_id
having min(change_date) > '2019-08-16';
