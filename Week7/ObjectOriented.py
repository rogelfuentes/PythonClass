# class Student:
#     firstName = "Rogel"
#     lastName = "Fuentes"

# studentFunction = Student()

# print (studentFunction)
# print(studentFunction.lastName)

# studentFunction.firstName = "Alfredo"

# print(studentFunction.firstName)

# ************

class StudentData:
    def __init__(self,first,last):
        self.firstName = first
        self.lastName = last

studentA = StudentData("Carlos","Lopez")
studentB = StudentData("Mario","Uzcategui")
studentC = StudentData("Lorenzo","Snow")

print(studentA.firstName, studentA.lastName)
print(studentB.firstName, studentB.lastName)
print(studentC.firstName, studentC.lastName)
