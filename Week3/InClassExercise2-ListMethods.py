# Exercise 2 – List Methods


# #2.1. Shapes (5 points)
# Create a list called shapes and set: shapes = ['square', 'circle'].
shapes = ['square', 'circle']
# Use append and add a triangle and print the list.
shapes.append("triangle")
print(shapes)
# Use insert and insert a rectangle and print the list.
shapes.insert(2, "rectangle")
print(shapes)
# Remove the rectangle and print.
shapes.remove("rectangle")
print(shapes)
# Use del on element 2 and print.
del shapes[2]
print(shapes)

 

# #2.2. Sorting (5 points)
# Using the sort function, sort this list in numerical order and print it:
ages = [27, 60, 14, 35, 3, 76]
ages.sort()
print(ages)

# Sort the following list in alphabetical order:
names = ["Quinn", 'John', "Amber", 'Kim']
names.sort()
print(names)

# Sort the following list in numerical order and print:
stats = [[3, 2], [1, 2], [1, 1], [3, 1]]
stats.sort()
print(stats)



# 2.3. Min-Max (5 points)
# Using the following list, print the min and max range of the list:
numbers = [6, 10, 3, 24, 79, 24]
print(max(numbers))
print(min(numbers))