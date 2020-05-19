class Student:

    def populate_fields(self):
      firstName, lastName = input("Please type in your name: ").split()
      assesmentGradeICT = float(input("Please type in your ICT Assesment Grade: "))
      homeworkGradeICT = float(input("Please type in your ICT Homework Grade: "))
      finalExamGradeICT = float(input("Please type in your ICT Final Grade: "))
      self.firstName, self.lastName = firstName, lastName
      self.assesmentGradeICT = assesmentGradeICT
      self.homeworkGradeICT = homeworkGradeICT
      self.finalExamGradeICT = finalExamGradeICT

newStudent = Student()
newStudent.populate_fields()

def overallICTGrade():
    if finalPercentage() >= 90 <= 100:
        return "A"
    elif finalPercentage() >= 80 <90:
        return "B"
    elif finalPercentage()>= 70 < 80:
        return "C"
    elif finalPercentage() >= 60 < 70:
        return "D"
    else:
        return "F"
    
def finalPercentage():
    grade = (newStudent.homeworkGradeICT * 0.25 + newStudent.assesmentGradeICT * 0.35 + newStudent.finalExamGradeICT * 0.40)
    return grade
##TEST for return value
##print (finalPercentage())

print("Hello, ", newStudent.firstName, newStudent.lastName, "your overall ICT grade is", overallICTGrade())

