x=[1,2,[3,4,5],6,7] #declare
print(x)
# [1,2,[3,4,5],6,7]
# 0, 1, 2[0,1,2],3,4

print(x[0])
print(x[3])
print(x[4])
print(x[2])
print(x[2][0])
print(x[2][1])
print(x[2][2])
#Slicing
print(x[0:4])
print(x[0:])
print(x[:4])
print(x[2:4])

#Practice
x=[4,5,6,23,[10,6,7,5]]
print(x[0])
print(x[3])
print(x[4][2])
print(x[4][0])
print(x[3])

#slincing
print(x[0:4])
#4,5,6,23 between
print(x[:4])
print(x[:0])
print(x[:5])
print(x[:7])
print(x[0:136])
print(x[4][0:2])
print(x[4][0:900])
print(x[4][-1])
print(x[4][2:-1])
q=[1,2,3,4,5]
print(q[-1])
print(q[1:-1])

g=[3,4,7,8,9,[0,1,5,6]]
print(g[-1])
print(g[-1][1])
print(g[-1][2])
print(g[-1][:300])

#Tests
n=[1,2,3,[4,[5,6,[7,8],0],67],90]
#67
print(n[3][2])
print(n[3][1][1])
print(n[3][1][2][1])
print(n[4])
print(n[3][1][2][0])
print(n[3][2])
print(n[3][1][3])

#Example 2
l=["a","b","c",["d","z","m",["e",["f","g"]]]]
print(l[3][3][1][1])
print(l[3][3][0])