# Exercise 2.1: (2.5 points)

# Write a program that asks the user for the value of a coin. Then determine what kind of coin they entered using this information.
# 1 = “Penny”
# 5 = “Nickle”
# 10 = “Dime”
# 25 = “Quarter”
# 50 = “Half dollar”

# Request the user to enter a value of a coin
userValue = float(input("Enter a coin value: "))

penny = 0.01
nickle = 0.05


# Provide a message if you enter any other value that does not match.
# Sample 1:
# Enter a coin value: 1
# That’s a penny!

# Sample 2:
# Enter a coin value: 80
# That’s not a valid coin!

 

# Exercise 2.2: (2.5 points)
# Write a program that asks the user for a number between 1 and 10 (inclusive). Then report to the user the following:
# If the number is even
# If the number is odd
# If the number is prime
# If the number is not prime
# Ensure that the user enters a number between 1 and 10 (you can print an error message if they supply an invalid number).
# Hint: We only care about 1 - 10, so just hardcode a prime number check for 2, 3, 5 and 7. You can use the 'or' operator in one 'if' condition. Use the modulus operator to test for odd/even.

# Pseudo code:
# Prompt the user for a number between 1 and 10.
# If the number is less than 1 or greater than 10, print error message. end program.
# Else,
# If the number is even, 
# print even.
# else, print odd.
# If the number is 2,3,5,7 print a prime message.
# else, print it's not prime.
# End program.
 

# Exercise 2.3: (2.5 points)
# Write a program that asks the user for the price of an item they are purchasing. Items are eligible for a discount based on their price as follows:
# $10 or less: no discount
# Between $10 and $50: 10% discount
# Over $50: 20% discount
# Ensure that you don't allow the user to enter negative values or zero as a price value.
# Exercise #2.4: (2.5 points)
# Write a program that asks the user to enter a starting number (integer), ending number (integer) and the word "even" or "odd". Then generate a customized printout based on their input.

# Sample:
# Starting number: 5
# Ending number: 15
# Even or Odd?: even

 
# 6
# 8
# 10
# 12
# 14

 

# Exercise #2.5: (3 points)
# Write a program that asks the user to enter in a number of products (as an integer). Then prompt the user for that number of prices and compute the total cost of all products.

# Sample:
# Enter a number of products: 3
# Enter price for product # 1: 100
# Enter price for product # 2: 200
# Enter price for product # 3: 300

# Total cost: 600

 
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
# Exercise #2.8: (3 points)
# Write a program that continually asks the user for the answer to a simple math question (2 + 2). If the user answers the question correctly you should congratulate them and end the program. If they answer the question incorrectly you should re-prompt them until they answer correctly.

# Sample:
# What is 2+2? 3
# Wrong, try again.
# What is 2+2? 5
# Wrong, try again.
# What is 2+2? 4
# Correct!

 

# Exercise #2.9: (3 points)
# Modify Exercise #8 so that your program prompts the user for a random addition problem instead of always asking them to answer "What is 2+2?".
# Pseudo code:
# Generate 2 random numbers, num1, num2.
# Enter while loop
# Prompt the user "what is num1 + num2" equal?
# check the answer, if the input value equals the num1 + num2 then print "Correct!"
# Else, print "Incorrect" and try again.
# End loop.