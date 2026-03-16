# day14_pm_answers.md

## Part C

### Q1 — Difference between RANK() and DENSE_RANK()

RANK() assigns the same rank to ties but skips numbers after a tie.
Example: 1, 2, 2, 4.

DENSE_RANK() also gives the same rank to ties but does not skip numbers.
Example: 1, 2, 2, 3.

This matters in business situations like leaderboards or sales rankings.
If two salespeople tie for 2nd place:

* RANK() means the next person becomes 4th.
* DENSE_RANK() means the next person becomes 3rd.

Companies usually prefer DENSE_RANK() when they want continuous ranking.

### Q2 — Consecutive purchases logic

The query groups transactions by month, then assigns row numbers per user.
By subtracting the row number from the month sequence, consecutive months collapse into the same group.
If a group contains 3 or more rows, the user purchased in 3 consecutive months.

### Q3 — Why window function optimisation works

The original correlated subquery runs once per row:

O(n²)

The window function computes department averages once per partition:

O(n)

So the window function version is significantly faster for large tables.

## Part D — AI Generated Interview Questions

### Question 1

Find the top 5 highest paid employees in each department.

Answer:

Use ROW_NUMBER with partition.

Common mistake:

Candidates forget PARTITION BY department, which causes the ranking to be global instead of per department.

### Question 2

Find the cumulative revenue per customer ordered by date.

Answer:

Use SUM(revenue) OVER(PARTITION BY customer ORDER BY date).

Common mistake:

Using GROUP BY which removes row-level data instead of calculating a running total.

### Question 3

Find the difference in salary between each employee and the previous employee in the same department.

Answer:

Use LAG(salary) OVER(PARTITION BY department ORDER BY salary).

Common mistake:

Forgetting ORDER BY inside the window function, which makes LAG meaningless.

### Evaluation

The questions are reasonably senior-level because they require knowledge of window functions and partitioning logic.

The common mistakes listed are realistic. During testing it is easy to forget PARTITION BY or ORDER BY when writing window functions, which leads to incorrect results.
