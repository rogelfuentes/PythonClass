# Exercise 2.1: (2.5 points)

# Write a program that asks the user for the value of a coin. Then determine what kind of coin they entered using this information.
# 1 = “Penny”
# 5 = “Nickle”
# 10 = “Dime”
# 25 = “Quarter”
# 50 = “Half dollar”

# Sample 1:
# Enter a coin value: 1
# That’s a penny!

# Sample 2:
# Enter a coin value: 80
# That’s not a valid coin!

# Request the user to enter a value of a coin
userValue = float(input("Enter a coin value in cents (Exam: 0.01): "))

penny = float(0.01)
nickle = float(0.05)
dime = float(0.10)
quarter = float(0.25)
halfDollar = float(0.50)

if userValue == penny:
    print("It is a Penny!")
elif userValue == nickle:
    print("It is a nickle!")
elif userValue == dime:
    print("It is a dime!")
elif userValue == quarter:
    print("It is a quarter!")
elif userValue == halfDollar:
    print("It is a halfDollar!")
# Provide a message if you enter any other value that does not match.
else:
    print("That’s not a valid coin!")


# Exercise 2.2: (2.5 points)
# Write a program that asks the user for a number between 1 and 10 (inclusive). Then report to the user the following:
# If the number is even
# If the number is odd
# If the number is prime
# If the number is not prime
# Ensure that the user enters a number between 1 and 10 (you can print an error message if they supply an invalid number).
# Hint: We only care about 1 - 10, so just hardcode a prime number check for 2, 3, 5 and 7. You can use the 'or' operator in one
# 'if' condition. Use the modulus operator to test for odd/even.

# Prompt the user for a number between 1 and 10.
userNumber = int(input("Pick an integer number from 1 to 10: "))

# If the number is less than 1 or greater than 10, print error message. end program.
if userNumber < 1 or userNumber > 10:
    print("The number you have provited is not in the range of 1 to 10")
else:
# If the number is even,
    if userNumber % 2 == 0:
# print even.
        print("The number", userNumber, "is even,")
        if userNumber == 2:
            print("and it is a prime number")
        else:
            print("and it is not a prime number")
    else:
# else, print odd.
        print("The number", userNumber, "is odd,")
        if userNumber == 3 or userNumber == 5 or userNumber == 7:
# If the number is 2,3,5,7 print a prime message.
            print("and it is a prime number")
        else:
# else, print it's not prime.
            print("and it is not a prime number")
# End program.


# Exercise 2.3: (2.5 points)
# Write a program that asks the user for the price of an item they are purchasing.
# Items are eligible for a discount based on their price as follows:
# $10 or less: no discount
# Between $10 and $50: 10% discount
# Over $50: 20% discount
# Ensure that you don't allow the user to enter negative values or zero as a price value.

# Validating input data
dataValidation = True

while dataValidation:
    itemPrice = float(input("Please, enter the full price of the item (Avoit '0' or negative numbers): $"))
    if itemPrice == 0:
        print("Error: item cannot be a value of cero")
        dataValidation = True
    elif itemPrice <= -1:
        print("Error: item cannot have a negative value")
        dataValidation = True
    else:
        dataValidation = False
        if itemPrice <= 10:
            print("There is no discont in this item. The total price is $" + str(itemPrice))
        elif itemPrice <= 50:
            totalDiscount = (itemPrice - (itemPrice * float(0.1)))
            print("You got 10% discout. The total price is $" + str(totalDiscount))
        elif itemPrice > 50:
            totalDiscount = (itemPrice - (itemPrice * float(0.2)))
            print("You got 10% discout. The total price is $" + str(totalDiscount))


# Exercise #2.4: (2.5 points)
# Write a program that asks the user to enter a starting number (integer),ending number (integer) and the word "even" or "odd". Then generate a customized printout based on their input.
# Sample:
# Starting number: 5
# Ending number: 15
# Even or Odd?: even
# 6
# 8
# 10
# 12
# 14

#  Collecting data
startNum = int(input("Enter a starting number (integer):"))
endNum = int(input("Enter an ending number (integer):"))
evenOdd = str(input("Even or Odd?:"))

# Procesing data
if evenOdd.lower() == "even":
    while startNum <= endNum:
        if startNum % 2 == 0:
            print(startNum)
            startNum += 1
        else:
            startNum += 1
elif evenOdd.lower() == "odd":
    while startNum <= endNum:
        if startNum % 2 != 0:
            print(startNum)
            startNum += 1
        else:
            startNum += 1
else:
    print("Error: you should type Even or Odd ")



# Exercise #2.5: (3 points)
# Write a program that asks the user to enter in a number of products (as an integer). Then prompt the user for that number of prices and compute the total cost of all products.

# Sample:
# Enter a number of products: 3
# Enter price for product # 1: 100
# Enter price for product # 2: 200
# Enter price for product # 3: 300

# Total cost: 600

numOfProd = int(input("Enter in a number of products (as an integer)"))
prodAccount = 1
totalCost = 0

while prodAccount <= numOfProd:
    subTotal = float(input(f"Enter price for product #{prodAccount}: "))
    prodAccount += 1
    totalCost += subTotal

print(f"Total cost ${format(totalCost, '.2f')}")




# Exercise #2.6: (3 points)
# Write a simple "shopping cart" program that asks the user for a series of product prices. Compute sales tax (7%) on each price and print out the new price to the user. Next, ask the user if they want to enter another price - if they do, repeat the process. If not, end the program.

# Sample:
# Enter an item price: 1.00
# Tax on this item is 0.07 ; total price: 1.07
# Enter another price? (yes or no): yes
# Enter an item price: 2.00
# Tax on this item is 0.14 ; total price: 2.14
# Enter another price? (yes or no): yes
# Enter an item price: 3.00
# Tax on this item is 0.21 ; total price: 3.21
# Enter another price? (yes or no): no


# Prompt the user to enter the price of the item.
anotherPrice = "yes"
# Enter loop, while the item is not equal to "done".
while anotherPrice == "yes":
    itemPrice = float(input(" Please, enter an item price: "))
    totalPrice = (itemPrice) + (itemPrice) * 0.07
    print(f"Tax on this item is 0.07 ; The total price is: ${format(totalPrice, '.2f')}")
    anotherPrice = input("Enter another price? (yes or no): ") 
    if anotherPrice != "yes":
        break
print("We are done!")


# Exercise #2.7: (3 points)
# Modify Exercise #7 so that your program also keeps track of the total amount spent in addition to total tax due.
# Sample:
# Enter an item price: 1.00
# Tax on this item is 0.07 ; total price: 1.07
# Enter another price? (yes or no): yes
# Enter an item price: 2.00
# Tax on this item is 0.14 ; total price: 2.14
# Enter another price? (yes or no): yes
# Enter an item price: 3.00
# Tax on this item is 0.21 ; total price: 3.21
# Enter another price? (yes or no): no
# -------
# Total amount due: 6.42
# Total tax due: 0.42

# Prompt the user to enter the price of the item.
anotherPrice = "yes"
# Enter loop, while the item is not equal to "done".
while anotherPrice == "yes":
    itemPrice = float(input(" Please, enter an item price: "))
    taxPrice = itemPrice * 0.07
    totalPrice = itemPrice + taxPrice
    print(f"Tax on this item is 0.07 ; The total price is: ${format(totalPrice, '.2f')}")
    totalPrice += totalPrice
    taxPrice += taxPrice
    anotherPrice = input("Enter another price? (yes or no): ") 
    if anotherPrice != "yes":
        break
print(f"Total mount due: ${format(totalPrice, '.2f')}, \nTotal tax due: ${format(taxPrice, '.2f')}")


# Exercise #2.8: (3 points)
# Write a program that continually asks the user for the answer to a simple math question (2 + 2). If the user answers the question correctly you should congratulate them and end the program. If they answer the question incorrectly you should re-prompt them until they answer correctly.

# Sample:
# What is 2+2? 3
# Wrong, try again.
# What is 2+2? 5
# Wrong, try again.
# What is 2+2? 4
# Correct!


addition = ""
while addition != 4:
    addition = int(input("What is 2+2? :"))
    if addition != 4:
        print("Wrong, try again!")
    else:
        print("Correct!")



# Exercise #2.9: (3 points)
# Modify Exercise #8 so that your program prompts the user for a random addition problem instead of always asking them to answer "What is 2+2?".

# Pseudo code:
# Generate 2 random numbers, num1, num2.
import random
num1 = random.randint(1,99)
num2 = random.randint(1,99)

# Enter while loop
addition = 1
while addition != 0:
# Prompt the user "what is num1 + num2" equal?
    answer = int(input("what is the sum of " + str(num1) + " + " + str(num2) + ": "))
# check the answer, if the input value equals the num1 + num2 then print "Correct!"
    num_sum = num1 + num2
    if answer != num_sum:
        print("Incorrect, try again!")
# Else, print "Incorrect" and try again.
    else:
        print("Correct")
# End loop.
        break