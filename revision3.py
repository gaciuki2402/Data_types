import json

class Matatu_Booking():
    def Booking_Procedure(self):
        self.Details=[]
        self.passengers=eval(input("Enter The Number Of Customers:"))
        for customer in range(self.passengers):
            if self.passengers>3:
                print("No space Available.")
                break
            else:

                fname=input("First Name:")
                lname=input("Last Name:")
                gender=input("Gender:")
                age=input("Age:")
                contact=input("Contact Number:")
                email=input("Email Address:")
                start=input("Start:")
                stop=input("Stop:")

                myDict={
                    "First Name":fname,
                    "Last Name":lname,
                    "Gender":gender,
                    "Age":age,
                    "Contact Number":contact,
                    "Email Address":email,
                    "Start":start,
                    "Stop":stop

                }

                self.Details.append(myDict)
                p=json.dumps(self.Details,indent=4)
                print(p)

p1=Matatu_Booking()
p1.Booking_Procedure()
print("The Above list of passengers will travel on Monday.")

