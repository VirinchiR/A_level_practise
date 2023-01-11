class student:
    def __init__(self, name ,dateOfBirth,examMark):
        self.name = name
        self.dateOfBirth= dateOfBirth
        self.examMark =examMark
    def displayExamMark(self):
        print("Student Name: " + self.name)
        print("Exam Mark" ,self.examMark)
myStudent = student("Virinchi Rawal", 27/8/2005, 70)

myStudent.displayExamMark()
