# #2.1. Composition Exercise: (5 points)
# The code provided below is utilizing composition, however, we can hide the delegation of the methods which makes the classes more encapsulated and streamlined.
# Rewrite the Person class, implementing additional methods called enroll() and assign_teaching() which hides the delegation of the other classes.


class Person():
    
    def __init__(self, first_name, last_name, uNID, student=None, teacher=None):

        self._first_name = first_name
        self._last_last = last_name
        self._uNID = uNID
        self.student = student
        self.teacher = teacher

    @property
    def firstName(self):
        return self._first_name

    @firstName.setter
    def firstName(self, value):
        self._first_name = value
    
    @property
    def lastName(self):
        return self._last_name

    @lastName.setter
    def lastName(self, value):
        self._last_name = value


class Student:
    def __init__(self):
        self.classes = []
    def enroll(self, course):
        self.classes.append(course)
    def schedule(self):
        return self.classes

class Teacher:
    def __init__(self):
        self.courses_taught = []
    def assign_teaching(self, course):
        self.courses_taught.append(course)

obj = Person("John", "DeGrey", "u77937732", Student(), Teacher())
obj.student.enroll("Python 6850")
obj.student.enroll("Econ 6000")
obj.teacher.assign_teaching("History")
print(obj.student.schedule())


    



# #2.2. Properties Exercise: (5 points)
# A property is a way of providing a class with virtual or protected attributes. 
# They can be a good way of hiding and protecting implementation details. Using 
# the below code, add a function called fullname(), make this a property add a 
# setter property. The fullname() property (getter) shall return the first and 
# last name concatenated together. The setter shall split the full name into first 
# and last name and set the class variables accordingly.

class Person():
    
    def __init__(self, first_name, last_name, uNID, student=None, teacher=None):

        self._first_name = first_name
        self._last_last = last_name
        self._uNID = uNID
        self.student = student
        self.teacher = teacher

    @property
    def firstName(self):
        return self._first_name

    @firstName.setter
    def firstName(self, value):
        self._first_name = value
    
    @property
    def lastName(self):
        return self._last_name

    @lastName.setter
    def lastName(self, value):
        self._last_name = value

    @property
    def fullname(self):
        return self._first_name + " " + self._last_name
    
    @fullname.setter
    def fullname(self, value):
        name = value.split(" ")
        _first_name = name[0]
        _last_name = name[1]

class Student:
    def __init__(self):
        self.classes = []
    def enroll(self, course):
        self.classes.append(course)
    def schedule(self):
        return self.classes

class Teacher:
    def __init__(self):
        self.courses_taught = []
    def assign_teaching(self, course):
        self.courses_taught.append(course)

obj = Person("John", "DeGrey", "u77937732", Student(), Teacher())
obj.student.enroll("Python 6850")
obj.student.enroll("Econ 6000")
obj.teacher.assign_teaching("History")
print(obj.student.schedule())

obj.fullname = "Thor Odinson"
print(obj.firstName)