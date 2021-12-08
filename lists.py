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