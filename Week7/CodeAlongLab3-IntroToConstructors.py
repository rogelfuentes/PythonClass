class Student:
    
    firstName = ""
    lastName = ""
    isGraduated = False

    def __init__(self, fName, lName):
       self.firstName = fName
       self.lastName = lName

    def sayHi(self):
        print("Hello", self.firstName, self.lastName)

    def formatName(self):
        return self.firstName + " " + self.lastName

studentA = Student("John", "DeGrey")
studentA.sayHi()
print(studentA.formatName())