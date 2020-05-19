class student():
    def __init__(self, firstName, lastName, homeworkGradeICT,
                 assesmentGradeICT, finalGradeICT):
        self.firstName, self.lastName = firstName, lastName
        self.assesmentGradeICT = assesmentGradeICT
        self.homeworkGradeICT = homeworkGradeICT
        self.finalExamGradeICT = finalExamGradeICT

    firstName, lastName = input("Please type in your name: ").split()
    ##lastName = ("Please type in your last name: ")
    assesmentGradeICT = float(input("Please type in your ICT Assesment Grade: "))
    homeworkGradeICT = float(input("Please type in your ICT Homework Grade: "))
    finalExamGradeICT = float(input("Please type in your ICT Final Grade: "))

    newStudent = student(firstName, lastName, homeworkGradeICT, assesmentGradeICT, finalGradeICT)
            
##def finalGrade(homeworkGradeICT, assesmentGradeICT, finalGradeICT):
    

##print("Hello, ", student().firstName, student().lastName, "your overall  ICT grade is ", percentageICT)
