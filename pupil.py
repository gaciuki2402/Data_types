class Grading:
    def pupilDetails(self):
        self.studentList={
    }
    self.number_of_students=eval(input("Enter the number of students in your class"))
    for student in range(self.number_of_students):
        name=input("Name:")
        age=input("Age:")
        adm=input("Adm:")
        self.studentList["Name"]=name
        self.studentList["Age"]=age
        self.studentList["Adm"]=adm
    return self.stu

