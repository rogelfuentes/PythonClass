# #1.1. Import functions: (5 points)
# Write a new function in your functions file (as noted above). Create 2 functions; one to convert a value from 
# Fahrenheit to celsius and the second function to convert from celsius to Fahrenheit, remember to return the values in the function statement.
# Create a new python file called ICE1.py. Using Import, import your new functions script in the ICE.py script.
# Using the print() function, test and invoke the celsius and Fahrenheit functions.


import MyFunction as func
print(func.CToF(30))
print(func.FToC(90))


# #1.2. NullToBooleanConverter: (5 points)
# Create a new function in your functions.py script called NullToBooleanConverter(). If null (None), return false, otherwise return true. (Hint: this can be done with one line of code using comparison operators)
# In the ICE1.py file and using the print() function, test and invoke the function using a non-null variable and a variable that is null.

val = None
print(func.NullToBooleanConvert(val))

 

# #1.3. Magic 8-Ball: (5 points)
# Create a new function in your functions.py script called getAnswer() that takes one numerical argument called answerNumber.
# use the following code inside the new getAnswer() function:

# if answerNumber == 1:
#     return 'It is certain'
# elif answerNumber == 2:
#     return 'It is decidedly so'
# elif answerNumber == 3:
#     return 'Yes'
# elif answerNumber == 4:
#     return 'Reply hazy try again'
# elif answerNumber == 5:
#     return 'Ask again later'
# elif answerNumber == 6:
#     return 'Concentrate and ask again'
# elif answerNumber == 7:
#     return 'My reply is no'
# elif answerNumber == 8:
#     return 'Outlook not so good'
# elif answerNumber == 9:
#     return 'Very doubtful'

# In the ICE1.py script, use the random generator and generate a number between 1 and 9. Pass the number into the getAnswer() function and print out the users fortune.

import random
r = random.randint(1,9)
fortune = func.getAnswer(r)
print(fortune)