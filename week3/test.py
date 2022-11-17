import student_generator
students = student_generator.generate_students(12)
for student in students:
    print(student.name, ": ", student.gender)
    print("number of courses: ", len(student.data_sheet.courses))