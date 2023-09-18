# Variable inside the class is called class variable
# variable is common to all the object the class

class laptop:
    
    displaySize="15.6 inch" # class variable
    
    def __init__(self,price,ram):
        self.price=price    
        self.ram=ram
        
    def info(self): 
        print("Price:", self.price)
        print("RAM:", self.ram)
        print("Display",self.displaySize)

lenovo=laptop(60000, "16GB")   
acer=laptop(45000,"8GB")

lenovo.info()
print()
acer.info()
