# class Student:
#     def __init__ (self, first, last):
#         self.first_name = first
#         self.last_name = last
#         self.grades = []

#     def say_hi(self):
#         print(f"Hi {self.first_name}")
#     def print_grades(self):
#         print(self.grades)
#     def add_grades(self, value):
#         self.grades.append(value)
#     def average(self):
#         return sum(self.grades)/len(self.grades)


# student1 = Student("Jimmy", "Thomson")
# student1.say_hi()
# student1.add_grades(100)
# student1.add_grades(80)
# student1.add_grades(90)
# average = student1.average()
# print(average)


# Restaurant

class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
    def describe_restaurant(self):
        print(f"Restaurant name: {self.name}")
        print(f"Restaurant cuisine: {self.cuisine}")
    def open_restaurant(self):
        print("The restaurant is opne")

class User:
    def __init__(self, first, last):
        self.first_name = first
        self.last_name = last

restaurant = Restaurant("PizzaHot", "Fast food")
restaurant.describe_restaurant()

