import xml.etree.ElementTree as ET

# Load and parse the XML file
tree = ET.parse("university_records.xml")
root = tree.getroot()

# Display university information
print("=" * 70)
print("UNIVERSITY RECORDS")
print("=" * 70)

print(f"University Name : {root.get('name')}")

# Campus information
campus = root.find("campus")

print("\nCAMPUS INFORMATION")
print("-" * 70)
print(f"Location   : {campus.findtext('location')}")
print(f"Established: {campus.findtext('established')}")
print(f"Website    : {campus.findtext('website')}")

# Department information
departments = root.find("departments")

for department in departments.findall("department"):
    dept_id = department.get("id")
    dept_name = department.findtext("name")
    hod = department.findtext("hod")
    building = department.findtext("building")

    print("\n" + "=" * 70)
    print(f"DEPARTMENT: {dept_id}")
    print("=" * 70)
    print(f"Name     : {dept_name}")
    print(f"HOD      : {hod}")
    print(f"Building : {building}")

    students = department.find("students")

    # Display each student
    for student in students.findall("student"):
        student_id = student.get("id")

        personal = student.find("personal_details")
        name = personal.find("name")

        first_name = name.findtext("first_name")
        last_name = name.findtext("last_name")

        print("\n" + "-" * 70)
        print(f"Student ID : {student_id}")
        print(f"Name       : {first_name} {last_name}")
        print(f"Gender     : {personal.findtext('gender')}")
        print(f"Date of Birth : {personal.findtext('date_of_birth')}")
        print(f"Phone      : {personal.findtext('phone')}")
        print(f"Email      : {personal.findtext('email')}")

        # Address
        address = personal.find("address")

        print("Address:")
        print(f"  Street     : {address.findtext('street')}")
        print(f"  City       : {address.findtext('city')}")
        print(f"  State      : {address.findtext('state')}")
        print(f"  Postal Code: {address.findtext('postal_code')}")

        # Academic information
        academic = student.find("academic_details")

        print("\nAcademic Details:")
        print(f"  Year    : {academic.findtext('year')}")
        print(f"  Semester: {academic.findtext('semester')}")
        print(f"  CGPA    : {academic.findtext('cgpa')}")
        print(f"  Advisor : {academic.findtext('advisor')}")

        # Courses
        courses = academic.find("courses")

        print("\nCourses:")
        print(
            f"  {'Code':<8} {'Course Name':<35} "
            f"{'Credits':<8} {'Marks':<7} {'Grade':<5}"
        )
        print("  " + "-" * 65)

        for course in courses.findall("course"):
            code = course.get("code")
            course_name = course.findtext("name")
            credits = course.findtext("credits")
            marks = course.findtext("marks")
            grade = course.findtext("grade")

            print(
                f"  {code:<8} {course_name:<35} "
                f"{credits:<8} {marks:<7} {grade:<5}"
            )

print("\n" + "=" * 70)
print("END OF UNIVERSITY RECORDS")
print("=" * 70)

