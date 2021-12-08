#Method 1
def my_function():
    a=2
    return a
print(my_function())

#method 2
def new_function():
    b=2
    print(b)
new_function()

#Example
def myName(name,age,uni):
    print(f"My name is {name} and i am {age} years old. I am a student at {uni}.")

#calling the function by its name
myName("Grace",20,"TTU")
myName("David",24,"UON")
myName("irene",20,"TUM")

#my Func
def myHobby(name,time):
    print(f"My hobby is playing {name} and i play it {time} in a week")
myHobby("lawn tennis","5.30 PM")
myHobby("football","5 times")

def addition(num1,num2):
    sum=num1+num2
    print(f"Addition: {sum}")

addition(6,7)

def subtraction(num1,num2):
    sub=num1-num2
    print(f"subtract:{sub}")
subtraction(500,900)
def multiplication(num1,num2):
    mul=num1*num2
    print(f"multiply:{mul}")
multiplication(3456,87754)
def division(num1,num2):
    div=num1/num2
    print(f"divide:{div}")
division(356273,761)

#create a function that takes year and determines whether its leap
#leap is divisible by 2,4 meaning remainder is 0
# %
def isLeaporNotLeap(year):
    if year%4==0 or year%2==0:
        print(f"{year} is leap.")
    else:
        print(f"{year} is not leap.")
isLeaporNotLeap(2000)
isLeaporNotLeap(2001)












def isleapornotisleapor_not_leap(year):
    if year%4==0 or year%2==0:
        print(f"{year} is leap")
    else:
        print(f"{year} is not leap")
isleapornotisleapor_not_leap(2078)

#Create a function that takes a number and determines whether its negative or positive

def ispositiveornegative(num):
    if num<0:
        print(f"{num} is negative")
    elif num>0:
        print(f"{num} is positive")
    elif num==0:
        print(f"{num} is zero")
    else:
        print("Invalid number")
ispositiveornegative(23476)
ispositiveornegative(-765)
ispositiveornegative(0)
