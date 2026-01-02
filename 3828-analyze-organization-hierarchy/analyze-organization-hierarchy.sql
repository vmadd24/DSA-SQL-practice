# Write your MySQL query statement below


with recursive hierarchy as (
    select
        employee_id,
        employee_name,
        manager_id,
        salary,
        1 as level
    from employees
    where manager_id is null

    union all

    select
        e.employee_id,
        e.employee_name,
        e.manager_id,
        e.salary,
        h.level + 1
    from employees e
    join hierarchy h
        on e.manager_id = h.employee_id
),

descendants as (
    select
        employee_id as manager_id,
        employee_id,
        salary
    from hierarchy

    union all

    select
        d.manager_id,
        e.employee_id,
        e.salary
    from descendants d
    join employees e
        on e.manager_id = d.employee_id
)

select
    h.employee_id,
    h.employee_name,
    h.level,
    count(d.employee_id) - 1 as team_size,
    sum(d.salary) as budget
from hierarchy h
join descendants d
    on h.employee_id = d.manager_id
group by
    h.employee_id,
    h.employee_name,
    h.level
order by
    h.level asc,
    budget desc,
    h.employee_name asc;
