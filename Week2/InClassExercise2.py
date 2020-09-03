#  Week 2: In-class exercise 2 - if conditions

#1. Password verification (2 points)
# Create a password variable and assign a value to this variable. (Such as Utes!)
passWord = str("Utes!")

# Prompt the user to enter a password, compare the user input with your variable.
enterPassword = str(input("Enter your password: "))

# Print out Access Granted or Access Denied depending if the value is true or false.
if passWord == enterPassword:
    print("Access granted!")
else:
    print("Access denied")



#2. Voting Age (2 points)
# Set a variable for voting age to 18. 
votingAge = 18

# Prompt a user for their age and returns whether they can vote. 
# If not, indicates how many more years until they can.
userAge = int(input("What is your age? "))
if userAge >= votingAge:
    print("You can vote!")
else:
    ageSubstraction = votingAge - userAge
    print("You can vote in", ageSubstraction, "years")


#3. Dress for Weather (2 points)
# Prompt the user to enter a temperature (What is the temperature?). Use integers, assume Fahrenheit. Use the following table to print out your message:
temperature = float(input("what is the temperature? "))

# Less than 40: Wear a warm coat.
if temperature < 40:
    print("Wear a warm coat!")

# Less than 70: Wear a light jacket.
elif temperature < 70:
    print("Wear a light jacket")

# Less than 100: Wear something cool.
elif temperature < 100:
    print("Wear something cool")

# 100 or greater: Prompt “Do you have air conditioning at home? (yes/no)”
elif temperature >= 100:
    airCond = input("Do you have air conditioning at home? (yes/no)").upper()

# If yes: print: “Stay at home.”
    if airCond == "YES":
        print("Stay at home!")
# If no: print: “Bummer, try a swimming pool.”
    else:
        print("Bummer, try a swimming pool")



