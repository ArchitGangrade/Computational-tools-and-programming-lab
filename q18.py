import sqlite3

con = sqlite3.connect("employees.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS employees(
    emp_id INTEGER PRIMARY KEY,
    name TEXT,
    designation TEXT,
    department TEXT,
    salary REAL
)
""")

cur.execute("SELECT department, SUM(salary) FROM employees GROUP BY department")
rows = cur.fetchall()

print("Department-wise Salary Report")

for row in rows:
    print("Department:", row[0], "Total Salary:", row[1])

department = input("Enter department: ")

cur.execute(
    "SELECT name, salary FROM employees WHERE department = ?",
    (department,)
)

rows = cur.fetchall()

print("\nEmployees in", department)

for row in rows:
    print("Name:", row[0], "Salary:", row[1])

con.close()

