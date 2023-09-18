# def __init__(self): -- syntax of constructor

class laptop:
    def __init__(self): # constructor
        # self represent the curren object, like "this" keyword in java
        self.price=0
        self.ram=""
        
    def info(self): #function
        print("Price:", self.price)
        print("RAM:", self.ram)

dell=laptop()   # object

dell.price=50000
dell.ram="8GB"

dell.info()

print()
#---------------------------------------------------------------------------

class animal:
    def __init__(self, color):  # constructor with parameter "color"
        self.color=color
    def display(self):
        print("Color of animal is:", self.color)

horse=animal("White")   # passing parameter
lion=animal("Orange")
dog=animal("Black")

horse.display()
lion.display()
dog.display()


        
