# Write your MySQL query statement below


with salary_classification as (
    select
        case
            when income < 20000 then "Low Salary"
            when income between 20000 and 50000 then "Average Salary"
            else "High Salary"
        end as category
    from Accounts
    union all
    select "Low Salary" as category
    union all
    select "Average Salary" as category
    union all
    select "High Salary" as category
)


select
    category,
    count(*)-1 as accounts_count
from salary_classification
group by category


