# Recovering from Errors

try:
    val = input("Type a number:")
    x = float(val)
    print("the next number is " + str(x + 1))
except:
    print('Hey! That is not a number!') 
    print('There was a problem in the Try statement, so it will run this')
else:
    print("If there is no problems in the Try statement, then it will run this")

# The finally statement

finally:
    print("Either way it will always run this statement")

