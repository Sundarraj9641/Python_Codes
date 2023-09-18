# function syntax
def add():  #function
    a=int(input("Enter the value for A: "))
    b=int(input("Enter the value for B: "))
    print("the addition of A and B is: ", a+b)

add()   #calling the function

print()
#-------------------------------------------------------------------
#function with argument and parameter

def greeting(name): # name -- variable
    print("Good Morning",name)

greeting("Sundarraj")   # passing a string

print()
#-------------------------------------------------------------------

def oddOrEven(num):
    if(num%2==0):
        print("Even")
    else:
        print("Odd")

oddOrEven(10)




