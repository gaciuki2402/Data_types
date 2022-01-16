def myFunct(n):
    sum=0
    for i in range(1,n+1):
        t=i+sum
        sum=t
        print(f"{i}--> {sum}")
myFunct(10)
