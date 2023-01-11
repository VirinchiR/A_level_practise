class student:
    def __init__(self, name ,dateOfBirth,examMark):
        self.name = name
        self.dateOfBirth= dateOfBirth
        self.examMark =examMark
    def displayExamMark(self):
        print("Student Name: " + self.name)
        print("Exam Mark" ,self.examMark)
myStudent = student("Virinchi Rawal", 27/8/2005, 70)
class partTimeStudent(student):
    def __init__(self, name, dateOfBirth,examMark):
        self.student = False
class fullTimeStudent(student):
    def __init__(self, name, dateOfBirth, examMark):
        student.__init__(self, name, dateOfBirth, examMark)
        self.__fullTimeStudent = True
myfullTimeStudent = student("Virinchi Rawal", 27/8/2005, 70)
myfullTimeStudent.displayExamMark()
mypartTimeStudent = student("Sergio Perez", 28/10/2005, 77)
mypartTimeStudent.displayExamMark()

