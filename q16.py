import sqlite3

con = sqlite3.connect("students.db")
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS students(
    roll_no INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    cgpa REAL
)
""")

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Delete Student")
    print("5. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        roll = int(input("Enter roll number: "))
        name = input("Enter name: ")
        dept = input("Enter department: ")
        cgpa = float(input("Enter CGPA: "))

        cur.execute("INSERT INTO students VALUES (?, ?, ?, ?)",
                    (roll, name, dept, cgpa))
        con.commit()
        print("Student added")

    elif choice == 2:
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()

        for row in rows:
            print(row)

    elif choice == 3:
        roll = int(input("Enter roll number: "))
        cur.execute("SELECT * FROM students WHERE roll_no = ?", (roll,))
        row = cur.fetchone()

        if row:
            print(row)
        else:
            print("Student not found")

    elif choice == 4:
        roll = int(input("Enter roll number: "))
        cur.execute("DELETE FROM students WHERE roll_no = ?", (roll,))
        con.commit()
        print("Student deleted")

    elif choice == 5:
        break

    else:
        print("Invalid choice")

con.close()

