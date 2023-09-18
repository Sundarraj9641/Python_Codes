#List
a=[]
a.append(1)
a.append(3)
a.append(8)
a.append(9)
a.append(56)
print(a)

print()


# get list of values from user
b=[]
for i in range(5):
    c=int(input())
    b.append(c)
print(b)


print()


# get the list of value from user and add the values

d=[]
add=0
for i in range(5):
    e=int(input())
    d.append(e)
    add+=d[i]
print(add)

