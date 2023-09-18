#<<<<<<<<<  ACCESS MODIFIERS <<<<<<<<<

# __ double underscore denotes "PRIVATE"
# _  single underscore denotes "PROTECTED"
# Without any underscore denotes "PUBLIC"

class Company:

    __companyName="Capgemini"   # Private variable

    def CompanyName(self):  # public function to access the private variable
        print(self.__companyName)

c1=Company()
c1.CompanyName()



    
