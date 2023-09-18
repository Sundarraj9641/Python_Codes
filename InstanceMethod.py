
# whenever we use the self keyword inside the function is called instance method

class Car:
    
    fuel="petrol"

    def __init__(self):
        self.brand=""
        self.airbag=4

    def setAirBag(self,airbag):     # instance method
        self.airbag=airbag

    def getAirBag(self):
        print(self.airbag)

tata=Car()

tata.setAirBag(6)
tata.getAirBag()



        
