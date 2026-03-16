Q1 — JOIN Question

Question:
Find employees who are leading a project and show their name, department name, and project name.

Query:
SELECT 
    e.name,
    d.department_name,
    p.project_name
FROM employees e
JOIN projects p
    ON e.id = p.lead_emp_id
JOIN departments d
    ON e.department_id = d.department_id;

Answer:
The query joins three tables. `employees` is joined with `projects` using the employee ID as the project lead, and `departments` is joined using the employee's department_id.


Q2 — NULL Handling Question

Question:
Show all projects and the employee leading them. If a project has no lead assigned, display 'Unassigned'.

Query:
SELECT 
    p.project_name,
    COALESCE(e.name,'Unassigned') AS lead_employee
FROM projects p
LEFT JOIN employees e
    ON p.lead_emp_id = e.id;

Answer:
`LEFT JOIN` ensures all projects appear even if no employee matches. `COALESCE()` replaces NULL values with 'Unassigned'.


Q3 — Aggregation + GROUP BY

Question:
Find the total salary paid per department.

Query:
SELECT 
    d.department_name,
    SUM(e.salary) AS total_salary
FROM departments d
JOIN employees e
    ON d.department_id = e.department_id
GROUP BY d.department_name;

Answer:
Employees are grouped by department and the total salary is calculated using SUM().


Q4 — Performance Question

Question:
Find all employees working in the IT department. Suggest a performance improvement if the employees table becomes very large.

Query:
SELECT *
FROM employees
WHERE department_id = 1;

Answer:
The query filters employees by department.  
To improve performance on large datasets, an index can be created:

CREATE INDEX idx_department
ON employees(department_id);

This allows the database to locate rows faster instead of scanning the whole table.


Q5 — Filtering with Aggregation

Question:
Find departments where the average employee salary is greater than 160000.

Query:
SELECT 
    d.department_name,
    AVG(e.salary) AS avg_salary
FROM departments d
JOIN employees e
    ON d.department_id = e.department_id
GROUP BY d.department_name
HAVING AVG(e.salary) > 160000;

Answer:
`HAVING` filters grouped results after aggregation. Only departments with average salary above 160000 are returned.


Evaluation

The questions are medium difficulty because they involve multiple SQL concepts such as JOINs, aggregation, NULL handling, indexing for performance, and HAVING filters. They are not trivial single-table queries but also not highly advanced topics like window functions or complex subqueries.

The answers are complete because they include both the SQL query and a short explanation of the logic used.