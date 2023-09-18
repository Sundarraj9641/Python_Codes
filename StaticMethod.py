
# Method which won't use instance and class variables is called Static Method

class Car:
    
    fuel="petrol"

    def __init__(self):
        self.brand=""
        self.airbag=4

    @staticmethod       # decorator
    def info():         # Static Method
        print("This is the example of Static Method")

ford=Car()
ford.info()








        
