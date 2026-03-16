
use my_database;

CREATE TABLE employees (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    department VARCHAR(50),
    salary INT,
    age INT
);


-- INSERT DATA


INSERT INTO employees VALUES
(1,'Alice','IT',70000,29),
(2,'Bob','HR',50000,34),
(3,'Carol','IT',90000,41),
(4,'David','Sales',60000,30),
(5,'Eva','HR',55000,28),
(6,'Frank','Sales',65000,33),
(7,'Grace','IT',80000,38),
(8,'Helen','Marketing',52000,26),
(9,'Ian','Marketing',58000,31),
(10,'Jack','HR',62000,45);


-- Select all employees


SELECT * FROM employees;


-- Employees with salary > 60000


SELECT name, salary
FROM employees
WHERE salary > 60000;


-- Average salary


SELECT AVG(salary)
FROM employees;


-- QUERY 4

SELECT name
FROM employees
WHERE department = 'IT';


-- Count employees per department


SELECT department, COUNT(*) AS employee_count
FROM employees
GROUP BY department;


-- Maximum salary

SELECT MAX(salary)
FROM employees;


-- Sort employees by salary

SELECT *
FROM employees
ORDER BY salary DESC;


-- Employees older than 30

SELECT name, age
FROM employees
WHERE age > 30;


-- Average salary by department


SELECT department, AVG(salary) AS avg_salary
FROM employees
GROUP BY department;


-- Employees with highest salary


SELECT *
FROM employees
WHERE salary = (SELECT MAX(salary) FROM employees);

-- Total salary per department

SELECT department, SUM(salary) AS total_salary
FROM employees
GROUP BY department;

-- Number of employees older than 30

SELECT COUNT(*)
FROM employees
WHERE age > 30;

-- Departments with avg salary > 60000

SELECT department, AVG(salary)
FROM employees
GROUP BY department
HAVING AVG(salary) > 60000;


-- Distinct departments

SELECT DISTINCT department
FROM employees;

-- Top 3 highest salaries

SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 3;

-- EXPLAIN QUERY PLANS

EXPLAIN
SELECT * FROM employees
WHERE salary > 60000;

EXPLAIN
SELECT department, AVG(salary)
FROM employees
GROUP BY department;

EXPLAIN
SELECT *
FROM employees
ORDER BY salary DESC
LIMIT 3;