class Principal:
    def dutyOfPrincipal(self):
        print("Report to Management")

class HoD(Principal):   # inherits Principal class
    def dutyOfHoD(self):
        print("Report to Principal")

class Professor(HoD):   # inherits HoD class
    def dutyOfProfessor(self):
        print("Report to HoD")

class Student(Professor):   # inherits Professor class
    def contact(self):
        print("Student can contact professor, HoD as well as Principal")

s1=Student()            # object of Student class

s1.contact()            # function inside Student class
s1.dutyOfProfessor()    # function inside Professor class
s1.dutyOfHoD()          # function inside HoD class
s1.dutyOfPrincipal()    # function inside Principal class




