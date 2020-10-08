import MyFunction as func

class YesNoBooleanValueConverter:

    def convert(self, val):
        if val:
            return "Yes"
        else:
            return "No"
    
    def convertBack(self, val):
        val = str(val).upper()
        if val == "Y" or val == "Yes":
            return True
        else:
            return False



class Student:

    firstName = ""
    lastName = ""
    isGraduated = False

studentA = Student()
studentA.firtName = "John"
studentA.lastName = "DeGrey"
studentA.isGraduated = True

# myList = list()
# myString = str()

vc = YesNoBooleanValueConverter()
gradStatus = vc.convert(studentA.isGraduated)

gradStatus1 = vc.convertBack("N")
print(studentA.firstName, studentA.lastName, " Is graduated: " + vc.convert(gradStatus1))