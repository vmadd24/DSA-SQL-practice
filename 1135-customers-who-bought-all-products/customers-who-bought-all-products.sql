# Write your MySQL query statement below

with distinct_customer_product as (
    select distinct *
    from Customer
)

select customer_id
from distinct_customer_product
group by customer_id
having count(*) = (select count(*) from Product)