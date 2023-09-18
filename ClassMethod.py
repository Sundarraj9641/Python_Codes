
# Class method comes with cls argument

class Car:
    
    fuel="petrol"

    def __init__(self):
        self.brand=""
        self.airbag=4

    @classmethod
    def changeFuel(cls):    # class method
        cls.fuel="electric power"   # change fuel type from petrol to electric power
        print(cls.fuel)
        

Car.changeFuel()






        
