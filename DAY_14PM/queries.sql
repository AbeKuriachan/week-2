-- day14_pm_queries.sql

-- Part A

-- 1. Running total: cumulative revenue per category ordered by date
SELECT
category,
order_date,
revenue,
SUM(revenue) OVER (
PARTITION BY category
ORDER BY order_date
) AS cumulative_revenue
FROM orders;

-- 2. Top 3 customers by revenue per city
SELECT *
FROM (
SELECT
city,
customer_id,
SUM(revenue) AS total_revenue,
ROW_NUMBER() OVER (
PARTITION BY city
ORDER BY SUM(revenue) DESC
) AS rn
FROM orders
GROUP BY city, customer_id
) t
WHERE rn <= 3;

-- 3. Month-over-month revenue change %
WITH monthly AS (
SELECT
DATE_TRUNC('month', order_date) AS month,
SUM(revenue) AS revenue
FROM orders
GROUP BY 1
)
SELECT
month,
revenue,
LAG(revenue) OVER (ORDER BY month) AS prev_month,
ROUND(
(revenue - LAG(revenue) OVER (ORDER BY month))
* 100.0
/ LAG(revenue) OVER (ORDER BY month),
2
) AS mom_change_pct
FROM monthly;

-- 4. Multi CTE: departments where all employees earn above company avg
WITH company_avg AS (
SELECT AVG(salary) AS avg_salary
FROM employees
),
dept_check AS (
SELECT
department_id,
MIN(salary) AS min_salary
FROM employees
GROUP BY department_id
)
SELECT d.department_id
FROM dept_check d
JOIN company_avg c
ON d.min_salary > c.avg_salary;

-- 5. 2nd highest salary per department (no window functions)
SELECT department_id, MAX(salary) AS second_highest_salary
FROM employees e1
WHERE salary < (
SELECT MAX(salary)
FROM employees e2
WHERE e2.department_id = e1.department_id
)
GROUP BY department_id;

-- Part B

-- Recursive CTE generating numbers 1 to 100
WITH RECURSIVE nums AS (
SELECT 1 AS n
UNION ALL
SELECT n + 1
FROM nums
WHERE n < 100
)
SELECT * FROM nums;

-- Use recursive numbers to fill missing dates in a time series
WITH RECURSIVE nums AS (
SELECT 0 AS n
UNION ALL
SELECT n + 1
FROM nums
WHERE n < 30
),
dates AS (
SELECT DATE '2024-01-01' + n AS dt
FROM nums
)
SELECT
d.dt,
COALESCE(SUM(o.revenue),0) AS revenue
FROM dates d
LEFT JOIN orders o
ON o.order_date = d.dt
GROUP BY d.dt
ORDER BY d.dt;

-- Part C Coding Question

-- users with purchases in 3 consecutive months
WITH monthly AS (
SELECT
user_id,
DATE_TRUNC('month', transaction_date) AS month
FROM transactions
GROUP BY user_id, month
),
seq AS (
SELECT
user_id,
month,
ROW_NUMBER() OVER (
PARTITION BY user_id
ORDER BY month
) AS rn
FROM monthly
)
SELECT user_id
FROM seq
GROUP BY user_id, month - rn * INTERVAL '1 month'
HAVING COUNT(*) >= 3;

-- Part C Optimised Query (window function version)

SELECT
name,
salary
FROM (
SELECT
name,
salary,
AVG(salary) OVER (PARTITION BY department) AS dept_avg
FROM employees
) t
WHERE salary > dept_avg;
