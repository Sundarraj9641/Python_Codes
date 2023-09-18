class calculation:  # class
    num1=3  #variables
    num2=5
    def add():  #function
        print("Addition a+b")
    def sub():
        print("Subtraction a-b")

a=calculation   # a -- object of class calculation
s=calculation   # s -- object of class calculation

a.add()     # invoke add function using object a
s.sub()     # invoke sub fucction using object s

print()


class mobile:   # class
    price=""    # variables
    size=""
    ram=""

samsung=mobile()    # objects
vivo=mobile()
oppo=mobile()

samsung.price="25,000"  # set values to variables
samsung.size="6 inch"
samsung.ram="8GB"

vivo.price="20,000"
vivo.size="5.7 inch"
vivo.ram="6GB"

oppo.price="23,000"
oppo.size="5.5 inch"
oppo.ram="12GB"

print("Samsung Price:",samsung.price)
print("Vivo Size:", vivo.size)
print("Oppo RAM:", oppo.ram)



