class Zoom_Meeting():
    def commitee_Details(self):
        self.Members=[]
        self.Number_of_members=eval(input("Enter the number of members:"))
        for member in range(self.Number_of_members):
            name=input("Enter Name:")
            RegNo=input("Enter Registration Number:")
            location=input("Enter Your Location:")
            age=input("Enter Your Age:")
            myDict={
                "Enter Name":name,
                "Enter Registration Number":RegNo,
                "Enter Your Location":location,
                "Enter Your Age":age,
            }

            self.Members.append(myDict)
            print(self.Members)

m1=Zoom_Meeting()
m1.commitee_Details()
print('The above members attended today\'s meeting.Thank You.')


