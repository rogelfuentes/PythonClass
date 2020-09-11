# Looping Through an Entire List
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
print("Thank you, everyone. That was a great magic show!")

# Using the range() Function
# “Python’s range() function makes it easy to generate a series of numbers. For example, you can use the range() function to print a series of numbers
for value in range(0, 5):
    print(value)
# “You can also pass range() only one argument, and it will start the sequence of numbers at 0. For example, range(6) would return the numbers from 0 through 5.
for value in range(6):
    print(value)

# Using range() to Make a List of Numbers
numbers = list(range(1,6))
print(numbers)

evenNumbers = list(range(2,11,2))
print(evenNumbers)

squares = []
for value in range(1, 11):
    square = value ** 2
    squares.append(square)
print(squares)

# Simple Statistics with a List of Numbers
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

# List Comprehensions
squares = [value**2 for value in range(1, 11)]
print(squares)

# Slicing a list
players = ["charles", "martina", "michael", "florence", "eli"]
print(players[1:3])
print(players[:4])
print(players[2:])
print(players[-3:])

# Looping Through a Slice
players = ["charles", "martina", "michael", "florence", "eli"]
for player in players[:3]:
    print(player.title())


# Copying a List
my_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_foods[:]

print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# Tuple
dimensions = (200, 50)
print(dimensions[0])

# Looping Through All Values in a Tuple
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

# Writing over a Tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)
