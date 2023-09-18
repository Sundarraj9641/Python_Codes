
class mobile:
    def smartphone(self):
        print("We can call")

class computer:
    def laptop(self):
        print("we can edit")

class tablet(mobile, computer): # tablet class inherits both mobile and computer class
    def spec(self):
        print("compact to use")


tab=tablet()        # object of tablet class
tab.spec()          # call function inside tablet class
tab.smartphone()    # call function inside mobile class
tab.laptop()        # call function inside computer class




