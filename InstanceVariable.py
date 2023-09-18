# Variable which represent the curren objectr is called Instance variable
# variable used inside constructor is called instance variable

class laptop:
    def __init__(self,price,ram): # constructor
        self.price=price    # Instance variable
        self.ram=ram
        
    def info(self): #function
        print("Price:", self.price)
        print("RAM:", self.ram)

dell=laptop(65000, "8GB")   # object
hp=laptop(55000,"16GB")

dell.info()
hp.info()
