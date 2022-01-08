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

#create a function that takes parametes of English,Kiswahili,Mathematics,Science,and Social Studies
#Output the total marks
#Output mean for the student marks
#Grade the pupil
def results_slip(Eng,Kisw,Maths,Sci,SST):
    TTM=Eng+Kisw+Maths+Sci+SST
    Mean=TTM/5
    print(f"Total:{Eng}+{Kisw}+{Maths}+{Sci}+{SST}={TTM}")
    print(f"Mean:{TTM}/{5}={Mean}")
    
results_slip(66,74,64,72,79)
