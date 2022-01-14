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
S1=Students_Results()
S1.Students_Details()
print("Welcome in Today's Lesson")

class Hostel_Bookings():
    def Residents_Details(self):
        self.ResidentsList=[]
        self.number_of_residents=eval(input("Evaluate number of residents:"))
        for resident in range (self.number_of_residents):
            if range(2):
                continue
            username=input("Name:")
            adm=input("AdmNO:")
            Year=input("Academic_Year:")
            hostel=input("Hostel Name:")
            room=input("RoomNo:")
            myDict={
                "Name":username,
                "AdmNO":adm,
                "Academin Year":Year,
                "Hostel Name":hostel,
                "RoomNO":room
            }
            self.ResidentsList.append(myDict)
            print(self.ResidentsList)

H1=Hostel_Bookings()
H1.Residents_Details()
print("...Hostel Booked Successfully...")










