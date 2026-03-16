## Q1 — Logical execution order of a SQL SELECT statement

Logical order:

1. FROM  
2. JOIN  
3. WHERE  
4. GROUP BY  
5. HAVING  
6. SELECT  
7. DISTINCT  
8. ORDER BY  
9. LIMIT / OFFSET

Why aliases matter:

Aliases defined in the SELECT clause are created after WHERE and GROUP BY are evaluated.  
Therefore, SELECT aliases cannot be used in WHERE. They can only be used in ORDER BY (and sometimes HAVING depending on the DB).


## Q2 — Single query (no subqueries or CTEs)

SELECT
    e.name,
    e.salary,
    AVG(e.salary) OVER (PARTITION BY e.department_id) AS department_avg_salary
FROM employees e
WHERE e.salary > AVG(e.salary) OVER ();


## Q3 — Debug the query

Bug:
Aggregate functions cannot be used in the WHERE clause.

Incorrect query:

SELECT department, AVG(salary) as avg_sal
FROM employees
WHERE AVG(salary) > 70000
GROUP BY department;

Correct query:

SELECT department, AVG(salary) AS avg_sal
FROM employees
GROUP BY department
HAVING AVG(salary) > 70000;

Explanation:
WHERE filters rows before grouping, while HAVING filters groups after aggregation.