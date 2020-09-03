import random

# Generate two ramdom numbers
num1 = random.randint(0,50)
num2 = random.randint(0,50)

# Ask the user what the sum of the generated numbers are
answer = int(input("what is the sum of " + str(num1) + " + " + str(num2) + ": "))

# add the sum together
num_sum = num1 + num2
if answer == num_sum:
    print("Correct!")

# Begin loop, while the answer does not equal the sum
while answer != num_sum:
    print("Incorrect, try again!")

# check if what the user entered matches the sum
    answer = int(input("What is the sum of " + str(num1) + " + " + str(num2) + ": "))
    num_sum = num1 + num2

# in correct, the print correct and end loop
# else, print incorrect and promt the user to try again
    if answer == num_sum:
        print("Correct")
     