import math
f=6
g=4
h=498
mult=f*g*h
print(f"{f}*{g}*{h} = {mult}")
div=f/g/h
print(f"{f}/{g}/{h} = {div}")

a=4895
b=2804
modulus=a%b
print(f"{a} % {b}={modulus}")
div=a/b
di=a//b
print(f"{a}/{b} = {div}")
print(f"{a}//{b} = {di}")
print(pow(div,10))
print("*"*67)
d=b/a
print(f"{b}/{a} = {d}")
print(round(d,4))
print(math.trunc(d))
sum=a+b
print(f"{a}+{b} = {sum}")
sub=b-a
print(f"{b}-{a} = {sub}")
print("*"*78)

def mocks_results(eng,kisw,scie,sst,math):
    Total_Marks=eng+kisw+scie+sst+math
    mean_marks=Total_Marks//5
    print(f"Total={Total_Marks}")
    print(f"Mean={mean_marks}")

m1=mocks_results(76,58,88,77,74)

def Salary(Basic_salary,allowances,commission):
    total_Salary=Basic_salary+allowances+commission
    salary_per_annum=total_Salary/12
    print(f"Total_Salary={total_Salary}")
    print(f"Average_salary={salary_per_annum}")
    print(round(salary_per_annum,4))
Salary(20000,80799,2000)
