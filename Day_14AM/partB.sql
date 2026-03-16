DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS employees;
DROP TABLE IF EXISTS departments;



CREATE TABLE departments (
department_id INT PRIMARY KEY,
department_name VARCHAR(50),
budget INT
);

CREATE TABLE employees (
id INT PRIMARY KEY,
name VARCHAR(50),
department_id INT,
salary INT,
age INT,
FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

CREATE TABLE projects (
project_id INT PRIMARY KEY,
project_name VARCHAR(100),
lead_emp_id INT,
budget INT,
start_date DATE,
end_date DATE,
FOREIGN KEY (lead_emp_id) REFERENCES employees(id)
);


INSERT INTO departments VALUES
(1,'IT',300000),
(2,'HR',150000),
(3,'Sales',200000),
(4,'Marketing',120000);


INSERT INTO employees VALUES
(1,'Alice',1,70000,29),
(2,'Bob',2,50000,34),
(3,'Carol',1,90000,41),
(4,'David',3,60000,30),
(5,'Eva',2,55000,28),
(6,'Frank',3,65000,33),
(7,'Grace',1,80000,38),
(8,'Helen',4,52000,26);



UPDATE employees
SET salary = salary + 100000
WHERE id > 0;


SELECT * FROM employees;

-- ===============================

INSERT INTO projects VALUES
(1,'AI Analytics Platform',1,200000,'2024-01-10','2024-06-30'),
(2,'HR Automation Tool',2,60000,'2024-02-01','2024-05-15'),
(3,'Cloud Migration',3,200000,'2024-03-05','2024-09-01'),
(4,'Sales Dashboard',4,70000,'2024-01-20','2024-04-30'),
(5,'Marketing Campaign AI',8,50000,'2024-02-10','2024-06-01');

-- ===============================

SELECT
e.name AS employee_name,
d.department_name,
d.budget AS department_budget,
p.project_name,
p.budget AS project_budget
FROM projects p
JOIN employees e
ON p.lead_emp_id = e.id
JOIN departments d
ON e.department_id = d.department_id;

-- ===============================

SELECT
d.department_name,
d.budget AS department_budget,
SUM(p.budget) AS total_project_budget
FROM departments d
JOIN employees e
ON d.department_id = e.department_id
JOIN projects p
ON e.id = p.lead_emp_id
GROUP BY d.department_name, d.budget
HAVING SUM(p.budget) > d.budget;
