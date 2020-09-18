#3.1. Split Number List (2.5 points)
# Use the string.split method create a list of numbers from the following string and then print the list to the screen.
# '10 67 123 46 20 18 36 250'
# Do the same thing for this string:
# '10,67,123,46,20,18,36,250'

numbers1 = '10 67 123 46 20 18 36 250'
splitedList = numbers1.split()
print(splitedList)

numbers2 = '10,67,123,46,20,18,36,250'
splitedList = numbers2.split(",")
print(splitedList)


# 3.2 Split Data into List (2.5 points)
# Use the string.split method create a list of numbers from the following string and then sum up the numbers.  Print the sum to the screen.
# '90,67,87,102,77,80'

numberSum = 0
numbers = '90,67,87,102,77,80'
splitedList = numbers.split(",")
for number in splitedList:
    numberSum += int(number)
print(splitedList)
print(numberSum)


# 3.3 Slice Lists (2.5 points)
# Use the slicing syntax of lists to get the first 4 numbers in the following list and print out the results.
# [1,2,3,4,5,6,7,8,9]

numbers = [1,2,3,4,5,6,7,8,9]
fourNumbers = numbers[:4]
print(fourNumbers)
 

# 3.4 Slice Lists with Increment (2.5 points)
# Use the slicing syntax of lists to get every other entry in the following list and print the results.
# ['a','b','c','d','e','f','g']

letters = ['a','b','c','d','e','f','g']
interval = letters[::2]
print(interval)
