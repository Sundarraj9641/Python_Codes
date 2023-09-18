# Do not allow duplicate
# Any type of data can be stored
# Key:Value pair

a={"Name":"sundarraj",
   "Age":22,
   "location":"Karur"
   }
print(a)

print()
#-----------------------------------------------------------------------

print(a.keys()) # print the keys

print()
#-----------------------------------------------------------------------

print(a.values())   # print the values

print()
#-----------------------------------------------------------------------

a["location"]="Chennai" #update the values
print(a)

    # Or
a.update({"location":"bangalore"})
print()
print(a)

print()
#-----------------------------------------------------------------------

a.pop("location")   #remove the key and value
print(a)
        #Or
print()
del a["Age"]
print(a)

print()
#-----------------------------------------------------------------------

a.clear()
print(a)



