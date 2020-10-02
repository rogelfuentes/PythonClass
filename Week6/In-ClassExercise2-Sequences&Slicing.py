# #1. Divide by zero exception (5 points)
# Create a function that will divide 2 numbers and return the result. The function will 
# accept 2 arguments. Use a try statement and the ZeroDivisionError exception type to catch 
# divide by zero errors. Inside the exception, print out “invalid argument”.

def divition(num1, num2): 
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("Invalit Argument")
results = divition(5,0)
print(results)


# #2. Basic exception handling (5 points)
# Handle the exception thrown by the code below by using try and except blocks.
# for i in ['a', 'b', 'c']:
#     print(i**2)
 
try:
    for i in ["a","b","c"]:
        print(i**2)
except:
    print("This is an error!")



# #3. try-except-finally (5 points)
# Handle the exception thrown by the code below by using try and except blocks. 
# Then use a finally block to print 'All Done.'

try:
    x = 5
    y = 3
    z = x/y
except:
    print("Error!")
finally: 
    print("All Done!")
 

# #4. try-except-else-finally (5 points)
# Write a function that asks for an integer and prints the square on it. Use a while loop with try, 
# except, else block to account for incorrect inputs.
# Output example:

# Input an integer: null
# An error occurred! Please try again!
# Input an integer: 2
# Thank you, your number squared is: 4

def ask():
    n=0
    while True:
        try:
            n = int(input("Enter a number: "))
            break
        except:
            print("Please try again! \n")
            continue
    result = n**2
    print("Your numer squared is: ", result)
ask()
