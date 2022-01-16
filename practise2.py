class Hostel_Bookings():
    def Residents_Details(self):
        self.ResidentsList=[]
        self.number_of_residents=eval(input("Evaluate number of residents:"))
        for resident in range (self.number_of_residents):
            if self.number_of_residents>3:
                print("Can\'t book for more than 3...")
                break
            else:
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
                print("...Hostel Booked Successfully...")
        print(self.ResidentsList)

H1=Hostel_Bookings()
H1.Residents_Details()
