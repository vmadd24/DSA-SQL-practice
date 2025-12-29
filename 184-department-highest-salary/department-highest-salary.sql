# Write your MySQL query statement below


with dep_emp_sal as (

    select
        d.name as Department,
        e.name as Employee,
        e.salary as Salary,
        RANK() over (partition by d.name order by e.salary desc) as sal_rank
    from Employee e inner join Department d
        on e.departmentId = d.id
)

select Department, Employee, Salary
from dep_emp_sal
where sal_rank = 1;