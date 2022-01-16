Units={1:"Calculus III",2:"Linear Algebra",3:"Data Base",4:"Vector Analysis",5:"Programming"}
for key, value in Units.items():
    print(key, value)
Foods={1:"Chapo",2:"Githeri",3:"Beans",4:"Pilau",5:"Rice",6:"Pojo",7:"Ugali"}
print(Foods.get(2))
print(Foods.get(4))
print(Foods.popitem())
print(Foods)
print(Foods.values())
print(list(Foods.items()))
print(len(Foods))
patient={"Name:":"Princess",
         "Age:":34,
         "Location:":"Nkabune",
         "Weight:":"90 pounds",
         "Children:":{"grace","kimberly"},
         "Diagnosis:":["TB","Cholera","Malaria"]
         }
# print(patient.values())

print(patient)
print(type(patient))
print(type(patient["Children:"]))
print("++++",patient.get("Children:"))
print(patient.get("Weight:"))
print(patient.get("Diagnosis:"))

for key, value in patient.items():
    print(key, value)
print(patient.get("Location:"))
print(type(patient.get("Diagnosis:")))
print(patient["Diagnosis:"])
print(patient.popitem())


