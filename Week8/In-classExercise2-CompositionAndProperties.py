# #2.1. Composition Exercise: (5 points)

# The code provided below is utilizing composition, however, we can hide the delegation of the methods which makes the classes more encapsulated and streamlined.

# Rewrite the Person class, implementing additional methods called enroll() and assign_teaching() which hides the delegation of the other classes.

# class Learner:
#     def __init__(self):
#         self.classes = []

#     def enrol(self, course):
#         self.classes.append(course)


# class Teacher:
#     def __init__(self):
#         self.courses_taught = []

#     def assign_teaching(self, course):
#         self.courses_taught.append(course)


# class Person:
#     def __init__(self, name, surname, number, learner=None, teacher=None):
#         self.name = name
#         self.surname = surname
#         self.number = number

#         self.learner = learner
#         self.teacher = teacher

# jane = Person("Jane", "Smith", "SMTJNX045", Learner(), Teacher())

# jane.learner.enrol("python")
# jane.teacher.assign_teaching("python")
 

# #2.2. Properties Exercise: (5 points)

# A property is a way of providing a class with virtual or protected attributes. They can be a good way of hiding and protecting implementation details. Using the below code, add a function called fullname(), make this a property add a setter property. The fullname() property (getter) shall return the first and last name concatenated together. The setter shall split the full name into first and last name and set the class variables accordingly.

# class Person():

#     def __init__(self, firstname, lastname):
#         self.first = firstname
#         self.last = lastname


#     def email(self):
#         return '{}.{}@email.com'.format(self.first, self.last)