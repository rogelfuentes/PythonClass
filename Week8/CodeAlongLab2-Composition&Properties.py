class Person:
    def __init__(self):
        self._first_name = None
        self._last_name = None
    
    
    @property
    def firstName(self):
        return self._first_name

    @firstName.setter
    def firstName(self, value):
        self._first_name = value

    @property
    def lastName(self):
        if self._last_name != None:
            return self._last_name
        else: return "Last name not set"
    
    @lastName.setter
    def lastName(self, value):
        self._last_name = value

a_person = Person()
a_person.firstName = "John"
a_person.lastName = "Degrey"
print(a_person.lastName, a_person.firstName)

class Student:
    def __init__(self, person):
        print(person.firstName)

a_student = Student(Person())

# ****************************************************

# class Student:
#     def __init__(self,person):
#         self.classes = []
#     def enroll(self, course):
#         self.classes.append(course)
#     def schedule(self):
#         return self.classes

# class Teacher:
#     def __init__(self):
#         self.courses_tau