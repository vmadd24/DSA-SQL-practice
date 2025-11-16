# Write your MySQL query statement below

select
    Department,
    Employee,
    Salary
from (
    select
        d.name as Department,
        e.name as Employee,
        e.salary as Salary,
        dense_rank() over(partition by e.departmentId order by e.salary desc) as dept_sal_rank
    from employee e inner join department d
        on e.departmentId = d.id
) t
where dept_sal_rank <= 3;
