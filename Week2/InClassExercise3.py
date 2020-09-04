# Week 2: In-class exercise 3 - while loops

# #1 Countdown (3 points)
# Asks the user for a number and then counts down by ones from that number until it gets to zero.
# Prints, "Done!" at the end.

userNumber = int(input("Type a number to counts down until it gets '0': "))
while userNumber >= 0:
    print(userNumber)
    userNumber = userNumber - 1
    # userNumber -= userNumber
else:
    print("It is Done!")

 

# #2 Shopping Total (3 points)
# Calculates the total including sales tax (8.875%) of a shopping trip.
# Create a total variable and a tax variable. Total the items calculated with tax. Be sure to test if the price is above zero.
# Continues to prompt the user to enter prices until they are done. Hint: enter a while loop until the user types ‘done’ at the prompt.
# Hint: Since we don't know how many times the loop will execute, it makes the most sense to use a 'while' loop. You will need to prompt the user in 2 different places. Once outside of the loop and again as the last line inside the while loop.

# Pseudo code:
# Create a few variables to hold the price of the item and the total.
total = 0
tax = 0.08875

# Prompt the user to enter the price of the item.
userItem = input("Enter the price of the item: ")

# Enter loop, while the item is not equal to "done".
while userItem != "done":

# Set a new variable to the price as a float value.
    price = float(userItem)

# Check if the price is 0 or higher, if less than 0 prompt the user to correct the price. (Hint: use a nested 'while' loop.
    while price <= 0:
        price = float(input("Please enter a positive number: $"))

# Add the price to the total variable.
    total += price
    
# Prompt the user to enter the price of the next item.
    userItem = input("Entert the price of the item or done: ")

# Add up the total and calculate the tax.
total += total * tax

# Format and display the total amount to the user.
# End program.
total = format(total, ".2f")
print("Your total $" + total )



