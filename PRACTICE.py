class Students_Results():
    def Students_Details(self):
        self.StudentsList=[]
        self.number_of_the_students=eval(input("Enter the number of the students:"))
        for student in range (self.number_of_the_students):
            name=input("Name:")
            age=input("Age:")
            adm=input("AdmNO:")
            myDict={
                "Name":name,
                "Age":age,
                "AdmNO":adm

            }
            self.StudentsList.append(myDict)
            print(self.StudentsList)
            print("Welcome in Today's Lesson")
S1=Students_Results()
S1.Students_Details()












