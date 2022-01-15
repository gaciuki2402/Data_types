angles={"right_angle":90,"acute_angle":180,"obtuse angle":70,"reflex_angle":360}
for key in angles:
    print(key, angles[key])
names={1:"grace",2:"irene",3:"davie",4:"rose"}
for key in names:
    print(key,names[key])
CountyNames={"Mombasa":"001","Meru":"012","Machakos":"016","Wajir":"008","Taita Taveta":"006"}
for key in CountyNames:
    print(key, CountyNames[key])
for key, value in CountyNames.items():
    print(key, value)
print("x"*56)
Fruits={"bananas:":"10 pieces","apples:":"4 pieces","oranges:":"20 pieces"}
print("Please Bring Me The Following:")
for key, value in Fruits.items():
    print(key, value)
Items={"biscuits:":"Ksh 20","water:":"Ksh 50","sweets:":"Ksh 15","soda:":"Ksh120"}
print("...SHOPPING LIST...")
for key, value in Items.items():
    print(key, value)
Personal_Details={"NAME:":"Belta","TEL:":2728292,"IDNO:":3839100,"AGE:":19,"EMAIL:":"belta@gmail","COURSE:":"Culinary Arts","LOCATION:":"Kiambu","SCHOOL:":"Boma"}
print("----MY PERSONAL INFO----")
for key, value in Personal_Details.items():
    print(key,value)
ItemsFruits={**Items,**Fruits}
print(ItemsFruits)
for key, value in ItemsFruits.items():
    print(key,value)
print("----END----"*56)
import itertools
options={
    "x":["a","b","c"],
    "y":[10,30,40]
}
keys=options.keys()
values=(options[key] for key in keys)
combinations=[dict(zip(keys, combination))for combination in itertools.product(*values)]
print(combinations)