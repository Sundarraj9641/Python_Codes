#simple for loop

for i in "Sundarraj":
    print(i)

#for loop in range

print() #this is to leave a blank line between output

for j in range(5):
    print(j)

print() #this is to leave a blank line between output

for k in range(1,10):   # it is starts from 1 and end at 9 (not 10)
    print(k)

# 2 table

for l in range(1,11):
    table=l*2
    print(l,"x 2 =", table)


# print even number between the range of 1 and 10
print() #this is to leave a blank line between output

for m in range(1,11):
    if(m%2==0):
        print(m)

# count the even number between the range of 1 and 10
print() #this is to leave a blank line between output
count=0
for n in range(1,11):
    if(n%2==0):
      count+=1
print(count)

#count numbers divisible by 3 and 5 in the range of 1 and 100
print() #this is to leave a blank line between output
divcount=0
for o in range(1,101):
      if(o%3==0 and o%5==0):
          divcount+=1
print(divcount)

# sum of 5 natural numbers
print() #this is to leave a blank line between output
num=0
for p in range(1,6):
    num+=p
    
print(num)


    











