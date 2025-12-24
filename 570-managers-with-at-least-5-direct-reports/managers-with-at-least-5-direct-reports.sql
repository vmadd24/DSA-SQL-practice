# Write your MySQL query statement below

with employee_manager_table as (
    select
        e1.id as employeeID,
        e1.name as employeeName,
        e1.managerId as managerID,
        e2.name as managerName
    from employee e1 inner join employee e2
        on e1.managerID = e2.id
)


select managerName as name
from employee_manager_table
group by managerName, managerID
having count(*) >= 5;

