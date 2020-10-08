# #2.1. The simplest class: (5 points)
# We will start with the simplest class you could ever write in Python. Create a class called Simplest() and use the pass statement.
# Answer the following questions:
# a. Using the code below, what type is this object?
# print(type(Simplest))
# b. Create an instance of Simplest to a variable called simp. What type is simp?

class Simplest():
    pass

print(type(Simplest))
simp = Simplest()
print(simp)


# #2.2. Person Class: (5 points)
# Create a new class called Person. Add 3 attributes (or fields) called first_name, middle and last_name.
# Add a function called format_name() and return all 3 attributes.
# (Hint: Use the same function we wrote in week 6).
# Create a new instance of the Person class, set the attribute fields and then call the format_name() function using print().

class Person:
    firstName = ""
    lastName = ""
    middle = ""

    def formatName(self):
        return (self.firstName + " " + self.middle + " " + self.lastName).title()

person = Person()
person.lastName = "Odinson"
person.firstName = "Thor"
person.middle = "E"
print(person.formatName())

# #2.3. Cylinder: (5 points)
# Create a Cylinder class using the class skeleton below. Fill in the code needed for each function.
# class Cylinder:
#     def set_height_radius(self, height, radious):
#         pass
#     def volume(self):
#         pass
#     def surface_area(self):
#         pass
                # Sample output should look like this:
                # mycyl = Cylinder()
                # mycyl.set_height_radius(2,3)
                # print(mycyl.volume())
                # 56.52
                # print(mycyl.surface_area())
                # 94.2
# Volume formula: height * pi(radius)^2
# Surface area formula: top = pi * radius^2 
# 2*top + (2*pi*radius*height)

class Cylinder:
    def setHeightRadious(self, height, radious):
        self.height = height
        self.radious = radious

    def volume(self):
        return self.height * 3.14 * (self.radious)**2

    def surfaceArea(self):
        top = 3.14 * (self.radious**2)
        return (2*top) + (2*3.14*self.radious*self.height)

mycyl = Cylinder()
mycyl.setHeightRadious(2,3)
print(mycyl.volume())
print(mycyl.surfaceArea()) 