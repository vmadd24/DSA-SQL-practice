# Write your MySQL query statement below

with first_occur as (
    SELECT
        product_id,
        MIN(year) as first_year
    FROM Sales
    GROUP BY product_id
)

SELECT
    s.product_id,
    fo.first_year,
    s.quantity AS quantity,
    s.price AS price
FROM Sales s JOIN first_occur fo
    ON s.product_id = fo.product_id AND s.year = fo.first_year


