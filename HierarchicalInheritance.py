# all sub classes inherits same super class

class college:
    def purpose(self):
        print("Going to study")

class Student1(college):    # inherits College class
    def std1(self):
        print("Student 1")
        
class Student2(college):    # inherits College class
    def std2(self):
        print("Student 2")

class Student3(college):    # inherits College class
    def std3(self):
        print("Student 3")

s1=Student1()
s1.purpose()

s2=Student2()
s2.purpose()

s3=Student3()
s3.purpose()


