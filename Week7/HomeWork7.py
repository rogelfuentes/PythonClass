# Exercise #1: (5 points)
# Here is a Person class definition:
# import datetime
# class Person:
#     def __init__(self, name, surname, birthdate, address, telephone, email):
#         self.name = name
#         self.surname = surname
#         self.birthdate = birthdate
#         self.address = address
#         self.telephone = telephone
#         self.email = email

#     def age(self):
#         today = datetime.date.today()
#         age = today.year - self.birthdate.year
#         if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
#             age -= 1
#         return age

# person = Person(
#     "Jane",
#     "Doe",
#     datetime.date(1992, 3, 12), # year, month, day
#     "No. 12 Short Street, Greenville",
#     "555 456 0987",
#     "jane.doe@example.com"
# )

# print(person.name)
# print(person.email)
# print(person.age())
 
# *************************************

# Explain what the following variables refer to, and their scope:
# Person: It is the class name that creates a blueprint 
# person: It is an instance of the class Student and holds the class call with arguments 
# surname: is the name of one of the arguments from the Constructor that is been retrieved from the function call
# self: it is a reference to the object is been created and where the values are been storage
# age (the function name): is the function name
# age (the variable used inside the function): Variable: it holds the subtraction  
# self.email: It is an instance variable 
# person.email: Assing a value to an instance
 
# ***************************************


# Exercise #2: (5 points)
# Rewrite the Person class so that a person’s age is calculated for the first time when a new person 
# instance is created, and recalculated (when it is requested) if the day has changed since the last time that it was calculated.
 
import datetime
class Person:
    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        today = datetime.date.today()
        age = today.year - self.birthdate.year
        if today < datetime.date(today.year, self.birthdate.month, self.birthdate.day):
            age -= 1
        return age

    def __str__(self):
        print("I'm a String")


person = Person(
    "Jane",
    "Doe",
    datetime.date(1992, 3, 12), # year, month, day
    "No. 12 Short Street, Greenville",
    "555 456 0987",
    "jane.doe@example.com"
)

person2 = Person(
    "John",
    "Carpinter",
    datetime.date(1945, 4, 18),
    "No. 19 Redwood Street, Gran Canion",
    "555 456 0987",
    "YYYY.doe@example.com"
)

print(person.name)
print(person.email)
print(person.age())
print("***************************")
print(person2.name)
print(person2.email)
print(person2.age())




# Exercise #3: (5 points)
# Create a new class called Square. Implement a constructor that takes a "side" parameter and initialize 
# it to a class member called "side". Add a function in the class called area(). The area() function will 
# return the side^2. Create an instance of the class and invoke the area() function to test it. Set the 
# instance variable "side" to a different value and invoke area() again.

 
# class Square:
#     def __init__ (self, side):
#         self.side = side

#     def area(self):
#         totalArea = self.side ** 2
#         return totalArea

# square = Square(2)
# print(f"The Square area is: {square.area()}")



# Exercise #4: (5 points)
# Create an instance of the Person class from exercise 1. Use the dir function on the instance. Then use the dir function on the class.
# What happens if you call the __str__ method on the instance? Verify that you get the same result if you call the str function with the
#  instance as a parameter.
# What is the type of the instance?
# What is the type of the class?
# Write a function which prints out the names and values of all the custom attributes of any object that is passed in as a parameter.
 




person3 = dir(Person(
    "John",
    "Carpinter",
    datetime.date(1945, 4, 18),
    "No. 19 Redwood Street, Gran Canion",
    "555 456 0987",
    "YYYY.doe@example.com")) 

print(person3)
print(dir(Person))
print(person3.__str__())


my_person = Person(
    "Juan",
    "Toledo",
    datetime.date(1960, 2,2),
    "128 S Tall St",
    "555 5555 5555",
    "ttteeett@gmail.com"
)

print(my_person)




# Exercise #5: (5 points)
# Write a Python class to reverse a string word by word.

 



# Exercise #6: (5 points)
# Write a Python class named Circle constructed by a radius and two methods which will compute the area and the perimeter of a circle.

 

# Exercise #7: (5 points)
# Write a Python class named Rectangle constructed by a length and width and a method which will compute the area of a rectangle.

 

# Exercise #8: (5 points)
# Create a Line class using the class skeleton below. Fill in the code needed for each function.
# (Hint: coor1, coor2 are tuples)
# class Line:

#     def __init__(self, coor1, coor2):
#         pass
#     def distance(self):
#         pass
#     def slope(self):
#         pass
 

# Sample output:
# coordinate1 = (3,2)
# coordinate2 = (8,10)

# li = Line(coordinate1, coordinate2)
# print(li.distance())
# 9.433981132056603

# print(li.slope())
# 1.6
# Slope Forumla:
# slope formula.png
# Distance Formula:
# distance formula.png

 

# Exercise #9: (5 points)
# Step 1:
# Write a function named collatz() that has one parameter named number.
# If number is even, then collatz() should print number // 2 and return this value.
# If number is odd, then collatz() should print and return 3 * number + 1.
# Step 2:
# Then write a program that lets the user type in an integer and that keeps calling 
# collatz() on that number until the function returns the value 1.
# Amazingly enough, this sequence actually works for any integer—sooner or later, using 
# this sequence, you’ll arrive at 1! Even mathematicians aren’t sure why.
# Your program is exploring what’s called the Collatz sequence, sometimes called “the simplest impossible math problem.”
# Remember to convert the return value from input() to an integer with the int() function; otherwise, it will be a string value.

