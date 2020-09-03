# Week 2: In-class exercise 1 - input()

#1. Change Calculator (2.5 points)
# Create a program that asks for the number of pennies, nickels, dimes, and quarters a person has.
# The program calculates the total and prints it to the screen with the $ sign.

# pseudocode:
# Prompt user for each coin and muliplying by the respective coin value..
pennies = (int(input("How many pennies do you have?"))) * (.01)
nickels = (int(input("How many nickels do you have?"))) * (.05)
dimes = (int(input("How many dimes do you have?"))) * (.1)
quaters = (int(input("How many quaters do you have?"))) * (.25)

# Total the sum of all values entered by user 
total = pennies + nickels + dimes + quaters

# format the total in currancy and print the amount of change the user has.
amount = format(total, ".2f")
print("You have $" + amount, " in change.")






#2. Currency Exchange (2.5 points)

# Calculates the value of another currency in US Dollars.
# Prompts the user to enter the current exchange rate between the two currencies.
# Asks the user to enter an amount to convert.
# Calculates and prints out the value in US dollars, formatted to two decimal places.

# pseudocode:
# Prompt user for exchange rate
exchRate = input("Enter a new exange rate: ")
exchRate = float(exchRate)

# Prompt user for currency amount to convert
amount = float(input("How much you would like to convert? "))

# Calculate currency, exchange rate * amount
total = exchRate * amount

# Print the amount in currency format to the user
total = format(total, ".2f")
amount = format(amount, ".2f")
print(amount, "of this currency is equal to ", "$" + total, "USD.")




