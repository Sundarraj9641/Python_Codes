
# super keyword is used to access the function or variable in inherited another class
class A:
        
    def Greeting(self):
        print("Hello A")

class B(A):     # class B inherits A

    def Greeting(self):
        super().Greeting()  # super Keyword
        print("Hello B")

b1=B()      # object of class B
b1.Greeting()





