dic={"name":"red","age":10}
print(dic)
dic["new_list"]={1,2,3,4}
print(dic)
dic["new_dic"]={"nested":1}
print(dic)
print("-"*67)
Details={"name":"Grace",
         "AdmNO":"TU01"}
print(f"{Details}")
Details["Course"]="MCS"
print(Details)
Details["Addition"]={
    "Units":7,
    "Contact":"073574727828",
    "Academic Year":4,
    "Dept":"MPS"

}
print(Details)
print("-"*67)
Person={"fname":"Joe","lname":"Juma","age":37,"children":["Doe","Betty","Pascal","Zoey"],"Pets":{"dog":"Lex","cat":"Sox"}}
print(Person)
print(Person["fname"])
print(Person["lname"])
print(Person["children"][1])
print(Person["children"][-1])
print(Person["children"])
print(Person["Pets"])
print(Person["age"])
print(Person["fname"]==["lname"])
print(len(Person["children"]))
print("-"*67)
d={int:1,float:2,bool:3}
print(d)
print(d[float])
d.clear()
print(d.get(float))
print(d)
angles={"right_angle":90,"acute_angle":180,"obtuse angle":70,"reflex_angle":360}
print(angles["reflex_angle"])
print("right_angle" in angles)
print("reflex_angle" not in angles)
print(angles.get("right_angle"))
print(angles.get("acute_angle"))
print(list(angles.items()))
print(angles)
print(angles.keys())
print(angles.values())
names={0:"Grace",1:"Grace",2:"Gaciuki",3:"Gaciuki"}
print(names)
print(names[2]==names[3])
print(names[0]==names[3])
print(len(names))
print(names.values())
print(names.pop(1))
print(names.pop(3))
print(names.popitem())
print(angles)






