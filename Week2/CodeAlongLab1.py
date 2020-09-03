
#  Part 1 Comments 
# This is a single line comment
"""
This is a multi-line comments

"""
# Part 2 value conversion
# We have three strings that are holding numbers:
a = "100"
b = "50.75"
c = "-3.2"

# Convert the string into numeric data
d = int(a)
e = float(b)
f = float(c)
answer = d + e + f
print("The sum of", a, b, "and", c, "is", answer)

# Part 3 input function

user_age = input("What is your age? ")
user_name = input("What is your name? ")
print("welcome to my program", user_name)
print("you are", user_age, " years old.")


