# Write your MySQL query statement below


select
    id,
    case
        when id%2 = 0 then lag(student, 1) over()
        when id%2 = 1 then lead(student, 1, student) over()
    end as student
from Seat