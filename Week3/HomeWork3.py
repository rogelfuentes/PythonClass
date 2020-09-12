# # Intro to Python 6850 - Homework #3

# # Exercise 1: (3 points)
# # Given the list below, write a program that counts the # of A’s (scores between 90 and 100). Extension: Count the # of B’s, C’s, D’s and F’s.
# # Hint: use an if-elif-else condition inside a for loop.
# grades = [90,100,70,45,76,84,93,21,36,99,100]

# # Creating a enty list for each grade
# fGradeList = []
# dGradeList = []
# cGradeList = []
# bGradeList = []
# aGradeList = []

# # Creating a grade account from 0
# fGradeAccount = 0
# dGradeAccount = 0
# cGradeAccount = 0
# bGradeAccount = 0
# aGradeAccount = 0

# # For look to the grades list
# for grade in grades:
#     if grade >= 90:
#         aGradeAccount += 1
#         aGradeList.append(grade)
#     elif grade >= 80:
#         bGradeAccount += 1
#         bGradeList.append(grade)
#     elif grade >= 70:
#         cGradeAccount += 1
#         cGradeList.append(grade)
#     elif grade >= 60:
#         dGradeAccount += 1
#         dGradeList.append(grade)
#     else:
#         fGradeAccount += 1
#         fGradeList.append(grade)

# # Print scores
# print(f"There are {aGradeAccount} in the grades list with an 'A' grade with the following scores: {aGradeList}")
# print(f"There are {bGradeAccount} in the grades list with an 'B' grade with the following scores: {bGradeList}")
# print(f"There are {cGradeAccount} in the grades list with an 'C' grade with the following scores: {cGradeList}")
# print(f"There are {dGradeAccount} in the grades list with an 'D' grade with the following scores: {dGradeList}")
# print(f"There are {fGradeAccount} in the grades list with an 'F' grade with the following scores: {fGradeList}")


# # Exercise 2: (3 points)
# # Given the following list of student test scores, apply a class "curve" to each score. The class curve is as follows:
# # 90 or above: no curve
# # 80 to 90: +2 points
# # 70 to 80: +5 points
# # Lower than 70: +8 points
# # Use the below test scores list:

# grades = [93, 74, 66, 98, 34, 75, 79, 83, 84, 91, 12, 69, 72]
# newGrades = []

# for grade in grades:
#     if grade >= 90:
#         newGrades.append(grade)
#     elif grade >= 80:
#         curveGrade = grade + 2
#         newGrades.append(curveGrade)
#     elif grade >= 70:
#         curveGrade = grade + 5
#         newGrades.append(curveGrade)
#     else:
#         curveGrade = grade + 8
#         newGrades.append(curveGrade)
# print(newGrades)


# # Exercise 3: (3 points)
# # Write a program that asks the user for daily sales figures for a full week (Sunday – Saturday). Store these values in a list and
# # print them out at the end of your program. Here's a sample running of your program:
# # Enter sales for Day #1: 100
# # Enter sales for Day #2: 200
# # Enter sales for Day #3: 300
# # Enter sales for Day #4: 400
# # Enter sales for Day #5: 500
# # Enter sales for Day #6: 600
# # Enter sales for Day #7: 700
# # Sales for the week: [100,200,300,400,500,600,700]

# weekSales = []

# for i in range(1,8):
#     daySale = float(input(f"Enter sales for Day #{i}: "))
#     weekSales.append(daySale)
# print(f"Sales for the week: {weekSales}")


# # Exercise #4: (3 points)
# # Given the following list, write a program that does the following:
# # Extract the first 3 elements of the list into a new list
# # Extract the characters b, c, and d into a new list
# # Extract the last 4 characters into a new list

# my_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# mylist1 = []
# mylist2 = []
# mylist3 = []


# for i in my_list[:3]:
#     mylist1.append(i)
# print(mylist1)

# for i in my_list[1:4]:
#     mylist2.append(i)
# print(mylist2)

# for i in my_list[-4:]:
#     mylist3.append(i)
# print(mylist3)


# # Exercise #5: (3 points)
# # Given the following lists, write a program that lets the user type in the name of a product. If the product name exists
# # in our inventory, you should print out that it is in our inventory. Otherwise you should print out that the product is not found.
# # Ensure that your program is case insensitive (i.e. searches for "Apple" or "apple" or "APPLE" should all succeed).

# products = ["apple", "pear", "peach", "banana"]
# custPro = (input(f"Please, type the name of the product you are looking for: ")).lower()

# if custPro in products:
#     print(f" {custPro.title()} is in our inventory!")
# else:
#     print(f" Sorry, {custPro.title()} is not in our inventory")


# # Exercise #6: (3 points)
# # Given these two lists, write a program that finds all elements that exist in both lists (i.e. the integer 2 exists in both lists).
# # Store your results in a list and print it out to the user. The expected answer is:
# # [1, 2, 3]
# # Two lists:

# a = [1,2,3,4,5]
# b = [2,3,10,11,12,1]

# a.sort()
# b.sort()

# newList = []

# for i in b:
#     aList = i
#     for I in a:
#         blist = I
#         if i == I:
#             newList.append(i)

# print(f"This elements exist in both of the lists: {newList}")


# # Exercise #7: (3 points)
# # Write a program that continually prompts a user to enter in a series of first names. The user can elect to stop entering
# # names when they supply the string "end." Store these first names in a list and print them out at the end of your program.
# # Extension: Prevent the user from entering duplicate names (hint: use the in operator).


# keepAsking = True
# nameList = []

# while keepAsking:
#     userName = input("Type a name then hit enter. If there is no more names type 'end' :")
#     if userName == "end":
#         keepAsking = False
#     elif userName in nameList:
#         print(f"{userName} is already in the list, type a new name.")
#     else:
#         nameList.append(userName)
# print(f"This is the new list of names: {nameList}")


# # Exercise #8: (3 points)
# # Continually ask the user for a product name. Next, see if that product name is included in the inventory list below. If it is,
# # remove the product from the list and then print the current list of products to the user. If the product is not on the list you
# # should alert the user that we do not currently carry the product in question. You can end the program when the list of products
# # is exhausted or when the user types the string "end."
# # products = ["apple", "pear", "peach", "banana"]

# product = True
# products = ["apple", "pear", "peach", "banana"]
# currentList = []

# while product:
#     # Continually ask the user for a product name.
#     if len(products) == 0:
#         print("Sorry, we are out off products")
#         product = False
#     else:
#         askProduct = str(input("Type the product name, other wise type 'end': "))
# # Next, see if that product name is included in the inventory list. If it is, remove the product from the list and then print the current list of products to the user.
#         if askProduct in products:
#             currentList.append(askProduct)
#             products.remove(askProduct)
# # currentList.append(virtualList)
#             print(currentList)
# # You can end the program when the list of products is exhausted or when the user types the string "end."
#         elif askProduct == "end":
#             product = False
# # If the product is not on the list you should alert the user that we do not currently carry the product in question.
#         elif askProduct not in products:
#             print("We do not currently carry the product")
# print("Game Over!")



# # Exercise #9: (3 points)
# # The lists below are organized in such a way that the item at position 0 in the first list matches with the item at position 0
# # in the second list. With this in mind, write a product price lookup program that works as follows:
# # Enter a product:  peanut butter
# # This product costs 3.99

# products = ['peanut butter', 'jelly', 'bread']
# prices = [3.99, 2.99, 1.99]
# product = True

# while product:
#     productName = input("Enter the product or type 'end' to finish the search: ")
#     if productName in products:
#         productIndex = products.index(productName)
#         print(f"This product cost: {prices[productIndex]}")
#     elif productName == "end":
#         product = False
#     else:
#         print("Sorry, we dont have that item in our inventory")
#         product = True
# print("Finished!")



# Exercise #10: (3 points)
# Write a program that asks a teacher for the number of students in his or her class. Next, ask the teacher how many assignments are
# given in this class. With this information prompt the user to enter in scores for each student and compute their average grade in the class.
# Hint: use a nested for loop for the assignments inside the student for loop. (For each student, iterate for each assignment)
# Sample:
# (Input sample)
# How many students in the class? 2
# How many assignments in the class? 2


# (Output sample)
# Student #1
# Assignment #1: 100
# Assignment #2: 90
# Student #1 earned a 95


# Student #2
# Assignment #1: 90
# Assignment #2: 80
# Student #2 earned a 85
