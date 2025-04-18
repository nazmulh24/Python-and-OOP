class Exam:
    def __init__(self, subject):
        self.subject = subject
        self.marks = 0

    def attend_to_exam(self):
        print(f"Attending the exam for {self.subject}.")

    def get_marks(self, marks):
        self.marks = marks
        print(f"Marks obtained in {self.subject}: {self.marks}")

    def sub(self):
        print(f"Subject: {self.subject}")


# Example usage
exam = Exam("Math")
exam.sub()
exam.attend_to_exam()
exam.get_marks(95)

phy = Exam("PHY")
phy.sub()
phy.attend_to_exam()
phy.get_marks(85)
