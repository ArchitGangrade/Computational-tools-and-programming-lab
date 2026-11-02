
import os
import xml.etree.ElementTree as ET

def create_or_modify_student_xml():
    filename = "students_info.xml"

    if os.path.exists(filename):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
        except ET.ParseError:
            root = ET.Element("students")
            tree = ET.ElementTree(root)
    else:
        root = ET.Element("students")
        tree = ET.ElementTree(root)

    if root.tag.lower() != "students":
        root.tag = "students"

    n = int(input("Enter the initial number of students to add: ").strip() or "2")

    for i in range(n):
        print(f"\nEnter details for Student {i + 1}:")

        while True:
            s_id = input("Enter Student ID: ").strip()
            if not s_id:
                print("Student ID cannot be empty.")
                continue

            exists = any(
                student.get("id") == s_id
                for student in root
                if student.tag.lower() == "student"
            )

            if exists:
                print("Student ID already exists. Enter a different ID.")
            else:
                break

        name = input("Enter Name: ").strip()
        department = input("Enter Department: ").strip()
        year = input("Enter Year: ").strip()
        email = input("Enter Email: ").strip()
        cgpa = input("Enter CGPA: ").strip()

        student = ET.SubElement(root, "student", id=s_id)
        ET.SubElement(student, "name").text = name
        ET.SubElement(student, "department").text = department
        ET.SubElement(student, "year").text = year
        ET.SubElement(student, "email").text = email
        ET.SubElement(student, "cgpa").text = cgpa

    tree.write(filename, encoding="utf-8", xml_declaration=True)
    print(f"\n[INFO] XML file '{filename}' updated successfully.")

    choice = input("\nDo you want to modify a student's record? (y/n): ").strip().lower()

    if choice == "y":
        target_id = input("Enter the Student ID to modify: ").strip()
        found = False

        for student in root:
            if student.tag.lower() != "student":
                continue

            if student.get("id") == target_id:
                found = True
                print("Student found! Enter new details. Press Enter to keep the old value.")

                name = input("New Name: ").strip()
                department = input("New Department: ").strip()
                year = input("New Year: ").strip()
                email = input("New Email: ").strip()
                cgpa = input("New CGPA: ").strip()

                if name:
                    student.find("name").text = name
                if department:
                    student.find("department").text = department
                if year:
                    student.find("year").text = year
                if email:
                    student.find("email").text = email
                if cgpa:
                    student.find("cgpa").text = cgpa

                tree.write(filename, encoding="utf-8", xml_declaration=True)
                print(f"[INFO] Student ID {target_id} updated successfully in XML.")
                break

        if not found:
            print("[ERROR] Student ID not found.")

if __name__ == "__main__":
    create_or_modify_student_xml()
