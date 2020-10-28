# #1.1. Ice Cream Shop inherits from Restaurant (5 points)

# Restaurant: Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: 
# a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces 
# of information, and a method called open_restaurant() that prints a message indicating that the restaurant is 
# open. Make an instance called restaurant from your class. Print the two attributes individually, and then call 
# both methods.

# Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that 
# inherits from the Restaurant class you wrote. Add an attribute of flavors to the __init__() for IceCreamStand. 
# Make a method called get_flavors() that will display the flavors for this ice cream shop. Create an instances 
# of the ice cream class and call the get_flavors() method.

# class Restaurant:
#     def __init__(self, name, cuisine_type):
#         pass
#     def describe_restaurant(self):
#         pass
#     def open_restaurant(self):
#         print(self.name + " is open for business")
# Usage Example:

# ice_cream = Ice_Cream_Stand("My Ice Cream Shoppe", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])
# ice_cream.describe_restaurant()
# ice_cream.open_restaurant()
# ice_cream.get_flavors()
 
# class Restaurant():
#     def __init__ (self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#     def describe_restaurant(self):
#         print(self.restaurant_name)
#         print(self.cuisine_type)
#     def open_restaurant(self):
#         print(self.restaurant_name + " is open for business")

# class Ice_Cream_Stand(Restaurant):
#     def __init__ (self, restaurant_name, cuisine_type, flavors):
#         Restaurant.__init__(self, restaurant_name, cuisine_type )
#         self.flavors = flavors
#     def get_flavors(self):
#         print("Here are the flavors: ", self.flavors)

# ice_cream = Ice_Cream_Stand("My Ice Cream Shoppe", "Ice Cream", ["Vanilla", "Chocolate", "Strawberry"])
# ice_cream.describe_restaurant()
# ice_cream.open_restaurant()
# ice_cream.get_flavors()



# #1.2. Admin inherits from User (5 points)
# Users: Make a class called User. Create two attributes called first_name and last_name, and then create several other attributes that are typically stored in a user profile. Make a method called describe_user() that prints a summary of the user’s information. Make another method called greet_user() that prints a personalized greeting to the user. Create several instances representing different users, and call both methods for each user.
# Admin: An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote. Add an attribute, privileges, that stores a list of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.

class User:
    def __init__(self, first_name, last_name, phone, address, dob):
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone
        self.address = address
        self.dob = dob
    
    def describe_user(self):
        print(self.first_name, self.last_name)
        print(self.phone)
        print(self.address)
        print(self.dob)

    def say_hi(self):
        print(f"Hi {self.first_name}, welcome to my program.")  

a = User("Tony", "Stark", "212-970-4133", "10880 Malibu Point", "5/29/70" )
a.describe_user() 
a.say_hi() 

class Admin(User):
    privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print("user can", self.privileges)

admin = Admin("Thor", "Odison", "To contact, send a raven", "123 Asgar Way", "964 A.D")
admin.describe_user()
admin.say_hi()
admin.show_privileges()
        