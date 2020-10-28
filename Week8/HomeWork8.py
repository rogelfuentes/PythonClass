# Exercise #1 : (10 points)
# Summoning Charm: The Summoning Charm (Accio) was a charm that summoned an object towards the caster.
# Consider the following code:

# class Spell:
#     def __init__(self, incantation, name):
#         self.name = name
#         self.incantation = incantation
#     def __str__(self):
#         return self.name + " " + self.incantation + "\n" + self.get_description()
#     def get_description(self):
#         return "No description"
#     def execute(self):
#         print(self.incantation)
# class Accio(Spell):
#     def __init__(self):
#         Spell.__init__(self, "Accio", "Summoning Charm")
# class Confundo(Spell):
#     def __init__(self):
#         Spell.__init__(self, "Confundo", "Confundus Charm")


# def get_description(self):
#     return "Causes the victim to become confused and befuddled."
# def study_spell(spell):
#         print(spell)


# spell = Accio()
# spell.execute()
# study_spell(spell)
# study_spell(Confundo())

# What are the parent and child classes here? 
#       -- Spell is the parent and the Accio and Confundo are the child --
# What does the code print out? (Try figuring it out without running it in Python) 
#       -- It prints: Accio, Summoning Charm Accio, Confundus Charm Confundo. --
# Which get description method is called when ‘study spell(Confundo())’ is executed? Why?
#       --  
# What do we need to do so that ‘print Accio()’ will print the appropriate description 
# (‘This charm summons an object to the caster, potentially over a significant distance’)? 
# Write down the code that we need to add and/or change.
#       -- 
 

# Exercise #2: (10 points)
# Using the code below, create a Bus object that will inherit all of the variables and methods 
# of the Vehicle class and display it.
# Expected Output: Vehicle Name: School Volvo Speed: 180 Mileage: 12

# class Vehicle:

#     def __init__(self, name, max_speed, mileage):
#         self.name = name
#         self.max_speed = max_speed
#         self.mileage = mileage

#     def transport(self):
#         print(f"Vehicule name: {self.name} \nSpeed: {self.max_speed} \nMillage: {self.mileage}")

# a = Vehicle("School Volvo", "180", "12")
# a.transport()


# Exercise #3: (10 points)
# Create a Bus child class that inherits from the Vehicle class. The default fare charge of any vehicle is seating capacity * 100. 
# If Vehicle is Bus instance, we need to add an extra 10% on full fare as a maintenance charge. So total fare for bus instance will 
# become the final amount = total fare + 10% of the total fare.
# Note: The bus seating capacity is 50. so the final fare amount should be 5550. You need to override the fare() method of a Vehicle 
# class in Bus class.
# Use the following code for your parent Vehicle class. We need to access the parent class from inside a method of a child class.


# class Vehicle:
#     def __init__(self, name, mileage, capacity):
#         self.name = name
#         self.mileage = mileage
#         self.capacity = capacity
#     def fare(self):
#         return self.capacity * 100

# class Bus(Vehicle):
#     def __init__ (self, name, mileage, capacity):
#         Vehicle.__init__(self, name, mileage, capacity)
#     def fare(self):
#         busCapasity =  self.capacity * 100
#         totalCapasity = (busCapasity * 0.1) + busCapasity 
#         return totalCapasity


# School_bus = Bus("School Volvo", 12, 50)
# print("Total Bus fare is:", School_bus.fare())


# Exercise #4: (10 points)
# Create a class called Numbers, which has a single class attribute called MULTIPLIER, and a constructor which takes the parameters x 
# and y (these should all be numbers).
# Write a method called add which returns the sum of the attributes x and y.
# Write a class method called multiply, which takes a single number parameter a and returns the product of a and MULTIPLIER.
# Write a static method called subtract, which takes two number parameters, b and c, and returns b - c.
# Write a method called value which returns a tuple containing the values of x and y. Make this method into a property, and write a 
# setter and a deleter for manipulating the values of x and y.
 

# class Numbers:

#     multiplier = 5

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def add(self):
#         return self.x + self.y
#     def multiply(self, a):
#         return (self.multiplier * a) 

#     @staticmethod
#     def subtract(b, c):
#         return b - c

#     @property
#     def value(self):
#         return self.x, self.y

#     # TODO: Create a setter and a deleter for value.
    
#     @value.setter
#     def value(self, value):
#         assert type(value) == int
#         # self._value = value

#     @value.deleter
#     def value(self, value):
#         assert type(value) == int
#         # self._value = value

# # var = 35
# # if var == 35:

# num = Numbers(5,6)
# num.value = 38


# print(num.add())
# print(num.multiply(2))
# print(num.subtract(4, 4))
# # print(num.value())
 


# Exercise #5 “Abstract classes” (10 points)
# Part 1:
# Write an “abstract” class, Box, and use it to define some methods which any box object should have: add, for adding any 
# number of items to the box, empty, for taking all the items out of the box and returning them as a list, and count, for 
# counting the items which are currently in the box. Write a simple Item class which has a name attribute and a value attribute 
# – you can assume that all the items you will use will be Item objects. Now write two subclasses of Box which use different 
# underlying collections to store items: ListBox should use a list, and DictBox should use a dict.
# Use this Box class to get started. All that is needed for this exercise is to follow the instructions in the TODO lines.

class Box:
    def add(self, *items):
        raise NotImplementedError()
    def empty(self):
        raise NotImplementedError()
    def count(self):
        raise NotImplementedError()

class Item:
    def __init__(self, name, value):
        # TODO: set the arguments name and value to self.name and self.value
        self.name = name
        self.value = value
        


class ListBox(Box):
    def __init__(self):
        self._items = []
    def add(self, *items):
        self._items.extend(items)
    def empty(self):
        # Create a new variable called items and set it equal to _items.
        self.items = _items
        # Set the private variable _items to a new list, this will make _items empty again.
        self._items = []
        # Return the new items variable.
        return items        
    def count(self):
        # Create a return statement to return the length of the items.
        return len(self._items) 


class DictBox(Box):
    def __init__(self):
        self._items = {}
    def add(self, *items):
        self._items.update(dict((i, i) for i in items))
    def empty(self):
        # create a new variable and set it equal to the dictionary values.
        dictValues = self._items
        # set the private variable _items to a new dictionary to make it empty.
        dictValues = {}
        # Return the new variable.
        return dictValues
    def count(self):
    #    Create a return statement to return the length of the items.
        return len(self._items)


def repack_boxes(*boxes):
    items = []
    # get all the items from each box, save it to a new variable called items, then empty the boxes.
    for box in boxes:
        items.extend(box.empty())
    # now we have all of the items in each box inside one list, traverse the list of items.
    while items:
        # for each box passed in, add an item to box, remove the item from the item list as its added to the box.
        # if we pass in 3 boxes to this function, that means we'll add 3 items to the boxes and remove those items 
        # from the list on each pass within the for loop.
        
        for box in boxes:
            try:
                # For each box in boxes: box.add(items.pop())
                for box in boxes:
                    box.add(items.pop())
            except IndexError:
                break
 

# Part 2:
# Write a function, repack_boxes, which takes any number of boxes as parameters, gathers up all the items they 
# contain, and redistributes them as evenly as possible over all the boxes. Order is unimportant. There are multiple 
# ways of doing this. Test your code with a ListBox with 20 items, a ListBox with 9 items and a DictBox with 5 items. 
# You should end up with two boxes with 11 items each, and one box with 12 items.






box1 = ListBox()
for i in range(20):
    item = Item(str(i), i)
    box1.add(item)


box2 = ListBox()
for i in range(9):
    item = Item(str(i), i)
    box2.add(item)


box3 = DictBox()
for i in range(5):
    item = Item(str(i), i)
    box3.add(item)


repack_boxes(box1, box2, box3)

print(box1.count())
print(box2.count())
print(box3.count())