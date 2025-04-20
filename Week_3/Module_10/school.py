class School:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.teachers = {}  # --> Dictionary --> "bangla": teacher_object
        self.classrooms = {}  # --> Dictionary --> "eight": classroom_object

    def add_classroom(self, classroom):
        self.classrooms[classroom.name] = classroom

    def add_teacher(self, subject, teacher):
        self.teachers[subject] = teacher

    def student_admission(self, student):
        classname = student.classroom.name
        self.classrooms[classname].add_students()

    @staticmethod
    def calculate_grade(marks):
        if marks >= 80 and marks <= 100:
            return "A+"
        elif marks >= 70:
            return "A"
        elif marks >= 60:
            return "B"
        elif marks >= 50:
            return "C"
        elif marks >= 50:
            return "D"
        else:
            return "F"

    @staticmethod
    def grade_to_value(grade):
        grade_map = {
            "A+": 4.00,
            "A": 3.50,
            "B": 3.00,
            "C": 2.50,
            "D": 2.00,
            "F": 0.00,
        }
        return grade_map[grade]

    @staticmethod
    def value_to_grade(value):
        if value == 4:
            return "A+"
        elif value >= 3.5:
            return "A"
        elif value >= 3.0:
            return "B"
        elif value >= 2.5:
            return "C"
        elif value >= 2.0:
            return "D"
        else:
            return "F"

    def __repr__(self):
        # All Classrooms
        # All Students
        # All Subjects
        # All Teachers
        # All Student Results
        pass
