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


# Repiting a list
variable = [1,2,3] * 2
# >>> [1,2,3,1,2,3]

# Concatenation two lists
list1 = [1,2,3]
list2 = [4,5,6]
list3 = list1 + list2
print(list3)
# >>>[1,2,3,4,5,6]

