-- Write your PostgreSQL query statement below
select
    C.visited_on,
    SUM(C.amount) over (order by C.visited_on rows between 6 preceding and current row) as amount,
    ROUND(AVG(C.amount) over (order by C.visited_on rows between 6 preceding and current row), 2) as average_amount
from (
        select
            visited_on,
            SUM(amount) as amount
        from Customer
        group by visited_on
        order by visited_on
    ) C   
offset 6