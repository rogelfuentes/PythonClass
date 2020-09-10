# Basic list

#1.1. Color List (2.5 points)

# Create a basic list called colors containing the names of six colors. Using the print() function, print out each of the following: the entire colors variable (not in a loop), the length, index 4, a range from 1 to 5, a range from -3 and on, multiply colors by 2.

# pseudo code:
# create a variable list of color names called colors.
colors = ["yellow", "blue", "red", "brown", "black", "white"]
# print the list.
print(colors)
# print the length
print(len(colors))
# print index 4
print(colors[4])
# print a range from 1 to 5 (using slice)
print(colors[1:5])
# print a range from -3 (using slice)
print(colors[-3:])
# print(colors * 2)
print(colors * 2)




#1.2. Color List Mutation (2.5 points)

# Using the same list as exercise #1.1 and using print statements for each: change the color name in element 5, 
# set element 2 to equal element 4, create a new color list and set three more color names then concatenate the 
# two lists together, set element 5 to equal your variable colors.
# Print the entire variable for each. Ex. print(colors).
# Example:
# colors[5] = 'indigo'
# print(colors)

# Change the color name in element 5
colors[5] = "Pink"
print(colors)

# Set element 2 to equal element 4
colors[2] = colors[4]
print(colors)

# Reate a new color list and set three more color names then concatenate the two lists together
newColorList = ["magenta", "green", "purpure"]
totalColorList = colors + newColorList
print(totalColorList)

# Set element 5 to equal your variable colors
colors[5] = "colors"
print(colors)


