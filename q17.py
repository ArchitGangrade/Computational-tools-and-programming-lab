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

while True:
    print("\n1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        emp_id = int(input("Enter employee ID: "))
        name = input("Enter name: ")
        designation = input("Enter designation: ")
        department = input("Enter department: ")
        salary = float(input("Enter salary: "))

        cur.execute(
            "INSERT INTO employees VALUES (?, ?, ?, ?, ?)",
            (emp_id, name, designation, department, salary)
        )
        con.commit()
        print("Employee added")

    elif choice == 2:
        cur.execute("SELECT * FROM employees")
        rows = cur.fetchall()

        for row in rows:
            print(row)

    elif choice == 3:
        emp_id = int(input("Enter employee ID: "))
        salary = float(input("Enter new salary: "))

        cur.execute(
            "UPDATE employees SET salary = ? WHERE emp_id = ?",
            (salary, emp_id)
        )
        con.commit()
        print("Employee updated")

    elif choice == 4:
        emp_id = int(input("Enter employee ID: "))

        cur.execute(
            "DELETE FROM employees WHERE emp_id = ?",
            (emp_id,)
        )
        con.commit()
        print("Employee deleted")

    elif choice == 5:
        break

    else:
        print("Invalid choice")

con.close()

