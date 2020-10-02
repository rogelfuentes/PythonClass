# 1. Name function (5 points)

# Write a function that takes 3 strings - first name, last name and middle initial. 
# Return one string that has the person’s full name.  Make sure that the first letter 
# of each name is capitalized (.title()) and then return the string. Use the .format() 
# string function in the return statement.

firstName = "rogel"
lastName = "fuentes"
middleName = "alfredo"

print(f"{firstName.title()} {middleName.title()} {lastName.title()}")
print("My name is {2} {0} {1}".format(middleName.title(),lastName.title(), firstName.title()))

def createName(first, last, middle):
    return(first + " " + middle + " " + last).title()
print(createName("rogel","fuentes", "A"))


# #2. String function practice (5 points)

    # 1. Using escape characters, print out the phrase “Welcome to O’Neil’s Boat Rentals!”

print("Welcome to O\'Neil\'s Boat Rentals!")

    # 2. Initialize one string variable to the following sentence: “Hello there! How are you? I'm doing fine."
    # Using the print() function and escape characters, make the output look exactly as below: (Be sure there’s a single quote in the word I’m.

    # Hello there!
    # How are you?
    # I'm doing fine.

val = "Hello there!\nHow are you?\nI\'m doing fine."
print(val)

    # 3. Initialize a string variable to “hello python” and print it out in all uppercase using a string function.

var = "hellow python".upper()
print(var)

    # 4. Write a small program using a ‘while’ loop (while True).
        # Prompt the user to enter their age.
        # Using a string function, check if the input is a decimal value, if true then break from the loop.
        # Continue prompting the user until a decimal number has been entered.

while True:
    age = input("Enter your age: ")
    if age.isdecimal():
        print("Nice!!")
        break
    print("Please enter a number for your age")
    
    # 5. Using a string function, print your first and last name with the * symbol on both sides of your name with a max of 25 characters.

print('Rogel Fuentes'.center(25, '*'))