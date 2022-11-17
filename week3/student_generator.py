import ex3_classes
import random, csv

names = ["bob","sam","gordon","alyx","hans","john", "anna"]
gender = ["male", "female"]
courses = []
courses.append(ex3_classes.Course("Computer science","1c","Guy Da Silva",30))
courses.append(ex3_classes.Course("Media","3b","Bob Hoskins",80))
courses.append(ex3_classes.Course("Math","2a","Charles Xavier",60))
image_urls = ["pic1.jpeg","pic2.jpeg","pic3.jpeg","pic4.jpeg","pic5.jpeg","pic6.jpeg","pic7.jpeg"]

def generate_students(n):
    students = []
    while (n > 0):
        n -= 1
        random_nums = range(1, 5)
        num_of_courses = random.choice(random_nums)
        data_sheet = ex3_classes.DataSheet(random.choices(courses, k=num_of_courses))
        for course in data_sheet.courses:
            course.grade = random.choice(ex3_classes.grades)

        students.append(ex3_classes.Student(random.choice(names) , random.choice(gender), data_sheet, random.choice(image_urls)))

    with open("students.csv", "w") as csv_file:
        fieldnames = ["student_name","gender","course_name","teacher","ects","classroom","grade","image_url"]
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writeheader()
        for student in students:
            for course in student.data_sheet.courses:
                writer.writerow({fieldnames[0]: student.name, fieldnames[1]: student.gender, fieldnames[2]: course.name
                , fieldnames[3]: course.teacher, fieldnames[4]: course.ETCS, fieldnames[5]: course.classroom, fieldnames[6]: course.grade
                , fieldnames[7]: student.image_url})

    return students


