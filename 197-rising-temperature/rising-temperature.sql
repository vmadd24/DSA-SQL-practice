# Write your MySQL query statement below

select w1.id
from weather w1 inner join weather w2
    on datediff(W1.recordDate, W2.recordDate) = 1
where w1.temperature > w2.temperature;