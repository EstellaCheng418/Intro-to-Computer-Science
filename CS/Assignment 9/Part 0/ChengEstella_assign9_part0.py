# Name: Estella Cheng
# Date: November 10, 2025
# Class Section: 001
# Assignment 09_Part #0: CS Rosters

print("NYU Computer Science Registration System")

# ----- Read class data -----
class_file = open("class_data.txt", "r")
class_data = class_file.read()
class_file.close()
id_and_title = class_data.split("\n")

class_ids = []
class_titles = []
for i in range(len(id_and_title)):
    parts = id_and_title[i].split(",")
    if len(parts)>=2:
        class_ids.append(parts[0])
        class_titles.append(parts[1])

# ----- Read enrollment data -----
enroll_file = open("enrollment_data.txt", "r")

enroll_data = enroll_file.read()
enroll_file.close()
enroll_info = enroll_data.split("\n")

enroll_course = []
enroll_last = []
enroll_first = []
for i in range(len(enroll_info)):
    parts = enroll_info[i].split(",")
    if len(parts)>=3:
        enroll_course.append(parts[0])
        enroll_last.append(parts[1])
        enroll_first.append(parts[2])

# ----- Ask user for course ID -----
course_id = input("Enter a course ID (i.e. CS0002, CS0004): ")

# ----- Check if course exists -----
if course_id not in class_ids:
    print("Cannot find this course")
else:
    index = class_ids.index(course_id)
    title = class_titles[index]
    print("The title of this class is:", title)

    # Collect all students enrolled in this course
    students = []
    for i in range(len(enroll_course)):
        if enroll_course[i] == course_id:
            students.append(enroll_last[i] + "," + enroll_first[i])

    # Print number of students
    print("The course has", len(students), "students enrolled")

    # Sort students alphabetically by last name
    students.sort()

    # Print students in the format * First Last
    for s in students:
        parts = s.split(",")
        last = parts[0]
        first = parts[1]
        print("*", first, last)
