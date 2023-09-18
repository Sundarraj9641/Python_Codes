
class testing:  # super class
    def info(self):
        print("To ensure the quality of the product")

class apiTesting(testing):  # sub class / api class inherits testing class
    def uses(self):
        print("To test the api")

a1=apiTesting() # create object of apiTesting class
a1.uses()   # call function inside the apiTesting class
a1.info()   # call function inside the testing class





