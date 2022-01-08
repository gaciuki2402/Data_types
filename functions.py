def myFunc():
    return 2+2
print(myFunc())

def multiplicationOfTwoNumbers():
    num1=2
    num2=9
    mult=num1*num2
    print(f"{num1} * {num2} = {mult}")
multiplicationOfTwoNumbers()

def divisionOfTwoNumbers(num=0,num1=0):#Parameters
    div=num/num1
    print(f"{num} / {num1} = {div}")
divisionOfTwoNumbers(78,9)
divisionOfTwoNumbers(90,9)


#Students info, parameter name,age,class, admNo
#Create two objects

def students_info(name,age,grade,admNO):
    print(f"My name is {name} and i am {age} years old.\nAm admNo {admNO}.\nAm in grade {grade}.")
students_info("Grace",16,8,5675)
students_info("Ireen",17,8,5678)