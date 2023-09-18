# Do not allow duplicate, Duplicate values will be remove.
# Any type of data can be stored
# We cannot modify the set item but we can add or remove items
# Sets are unordered
# add(), update(), remove(), pop()

a={1,2,3,4,1}
print("Duplicate value is removed", a)

print()
#------------------------------------------------------------------------

b={10,20,30,40}
b.add(50)   # element 50 is added to the set
print("Element is added", b)

print()
#------------------------------------------------------------------------

b.remove(30) # element 30 is removed
print("Element is removed",b)
