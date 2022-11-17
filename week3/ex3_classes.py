grades = [0,2,4,7,10,12]
class Student():
    def __init__(self, name, gender, data_sheet, image_url):
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.image_url = image_url

    def get_avg_grade(self):
        grades = self.data_sheet.get_grades_as_list()
        return sum(grades) / len(grades)

class DataSheet():
    def __init__(self, courses):
        self.courses = courses

    def get_grades_as_list(self):
        grades = []
        for course in self.courses:
            if course.grade is not None:
                grades.append(course.grade)

        return grades

class Course():
    def __init__(self, name, classroom, teacher, ETCS, grade=None):
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ETCS = ETCS
        self.grade = grade