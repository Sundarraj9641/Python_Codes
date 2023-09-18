
a=[1,2,3,4,5]
a.append(6) #append() -- add the element in the list
print("append is used",a)

print()
#---------------------------------------------------------------------------

b=[9,8,7,6,5]
b.insert(1,20)  #insert(0,20) -- insert the value 20 at index 1
print("insert is used",b)

print()
#---------------------------------------------------------------------------

c=[12,23,43,56,76]
c[1]=5  # Replace the element at index 1 with 5
print("replace is used",c)

print()
#---------------------------------------------------------------------------

d=[1,4,7,9,2]
d.pop(2)    # pop(2) -- remove the element at the index 2
print("pop is used",d)

print()
#---------------------------------------------------------------------------

e=[1,2,3,4,5]
f=[6,7,8,9,10]
e.extend(f) # extend() -- join the list f with list e
print("extend is used",e)
