
# Accessing Elements in a List
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)
print(bicycles[0])
print(bicycles[-1])
print(bicycles[2].title())

# Using Individual Values from a List
message = f"My first bicycle was a {bicycles[0].title()}."
print(message)

# Try it yourself 1
names = ["paul", "carlos", "robert", "alejangro"]
print(f"Hey, how have you been, {names[0].title()}?")

# Changing, Adding, and Removing Elements
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

# Changing
motorcycles[0] = 'ducati'
print(motorcycles)

# Adding
motorcycles.append('ducati')
motorcycles.append("expo")
print(motorcycles)

# Adding with an emty list
motorcycles = []
motorcycles.append('ducati')
motorcycles.append("expo")
motorcycles.append("another")

# Inserting Elements into a List
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

# Removing an Item Using the del Statement
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

# Removing an Item Using the pop() Method
colors = ["Yellow", "Blue", "Red"]
print(colors)
takeOffOneElement0 = colors.pop()
print(f"It take the last item by default, {takeOffOneElement0.lower()}")
print(colors)
takeOffOneElement = colors.pop(0)
print(colors)
print(takeOffOneElement)

# Removing an Item by Value
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('ducati')
print(motorcycles)

tooExpensive = "honda"
motorcycles.remove(tooExpensive)
print(motorcycles)
print(f"\nAn {tooExpensive.title()} is too expensive for me.")
print("By defaul .remove() remove the first in the list")

# Repiting a list
variable = [1,2,3] * 2
print(variable)

# Concatenation two lists
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)
# >>>[1,2,3,4,5,6]

# Organizing a List
# sort()
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
cars.sort(reverse=True)
print(cars)

# Sorting a List Temporarily with the sorted() Function
# To maintain the original order of a list but present it in a sorted order, you can use the sorted() function.
# The sorted() function can also accept a reverse=True argument if you want to display a list in reverse alphabetical order.
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)

# Printing a List in Reverse Order
# Notice that reverse() doesn’t sort backward alphabetically; it simply reverses the order of the list
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

# “Finding the Length of a List
# You can quickly find the length of a list by using the len() function. The list in this example has four items, so its length is 4
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(len(cars))

# Accessing the last item: “The index -1 always returns the last item in a list, in this case the value 'suzuki
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles[-1])
