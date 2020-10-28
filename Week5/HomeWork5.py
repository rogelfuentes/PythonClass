# Exercise #1: (5 points)
# Write a program that generates the following pattern. Use functions to break up the problem into reusable blocks of code.
# Code Example:
# def topOrBottom():
#     print ("#####")
# Output:

# #####
# #      #
#   # #
#    #
#   # #
# #      #
# #####

def topBottom():
    print("#######")
def x4():
    print(" #   # ")
def x2():
    print("  # #   ")
def x1():
    print("   #    ")

topBottom()
x4()
x2()
x1()
x2()
x4()
topBottom()


# Exercise #2: (5 points)

# Write a function that converts a number from feet to inches (12 inches in a foot) 
# and another function that converts feet to meters (0.3048 meters in a foot). Each 
# function should accept a single argument and use that argument to calculate the conversion 
# and print the result. Next, write a program that generates the following output - 
# make sure to use your functions in your program!

# numbers = [0,1,2,3,4,5,6,7,8,9]

# for number in numbers:
#     def convertion(numbers):
#         inches =  numbers * 0.0833
#         meters = inches * 39.3701
#         print(f"{numbers} foot is equal to {inches} inches and {format(meters, '.2f')} meters" )
#     convertion(number)

numbers = [0,1,2,3,4,5,6,7,8,9]

for number in numbers:
    def convertion1(numbers):
        inches =  numbers * 0.0833
        print(f"{numbers} foot is equal to {inches} inches")
    def convertion2(numbers):
        inches =  numbers * 0.0833
        meters = inches * 39.3701
        print(f"{inches} inches is iqual to {format(meters, '.2f')} meters" )
    convertion1(number)
    convertion2(number)



# Exercise #3: (5 points)

# Write a function that rolls two dice. Your function should be designed to accept a single argument 
# (an integer) and generate two die rolls between 1 and the number supplied. Your function should then 
# return the two rolls in ascending order. Next, write a program that rolls 5 sets of dice with different 
# sides. Here's a sample running of your program:

# 6 sided dice roll: 2 & 4
# 7 sided dice roll: 3 & 4
# 8 sided dice roll: 1 & 8
# 9 sided dice roll: 7 & 7
# 10 sided dice roll: 4 & 6


sides = int(input("Number of sides of the dice is: "))

for setes in range(1,6):

    def random(sides):
        import random
        num1 = random.randint(1,sides)   
        return num1

    for i in range(1,2):
        dice1 = random(sides)
        dice2 = random(sides)
        i += 1
    
    setes += 1
    sides += 1
    print(f"{sides} sided dice roll: {dice1} & {dice2}")




sides = int(input("Number of sides of the dice is: "))

def random(sides):
    import random
    num1 = random.randint(1,sides)
    print(num1)    
random(sides)


# Exercise #4: (5 points)
# Guess the number
# Prompt the user to guess a number. Check in input from the user against the secret number 
# that was randomly generated. Limit the guesses to 6 chances. If the user correctly guesses, 
# then print "Good job! You guessed my number in x guesses!" Else, if they failed to guess 
# correctly, print "Nope. The number I was thinking of was x".
# Use the following code to get you started:

# This is a guess the number game.
import random
# use the random.randint() function to generate a random number between 1 and 20.
secretNumber = random.randint(1, 20)

print('I am thinking of a number between 1 and 20, you have 6 chances to get the number')

guesses = 0

# Ask the player to guess 6 times.
for guesses in range(1, 7):
    guessNum = int(input("Make a guess: "))
    if guessNum == secretNumber:
        print(f"{secretNumber} is the right one, good job!" )
        break
    elif guessNum < secretNumber:
        print("Your guess is too low!")
    elif guessNum > secretNumber:
        print("Your guess is too high!")
    
print("The number of guesses: ", guesses)

# Sample output:

# I am thinking of a number between 1 and 20.
# Take a guess.
# 4
# Your guess is too low.
# Take a guess.
# 18
# Your guess is too high.
# Take a guess.
# 10
# Your guess is too low.
# Take a guess.
# 15
###### "Good job! You guessed my number in 4 guesses!"