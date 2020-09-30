# #2.1. Sum of numbers (3 points)
# Write a function that takes a list of numbers and returns the sum of the numbers.

def numList(a,b,c,d,e,f):
    return a+b+c+d+e+f
numList(1,2,3,4,5,6)

numbers = [2,45,67,24,64,29, 5]
def numSum(numbers):
    total = 0
    for i in numbers:
        total += i
    print("The sum of the numbers in the list is: ", total)
numSum(numbers)

# #2.2. Number power (3 points)
# Write a function that takes two integers and raises the first number to the power 
# of the second number and returns the result.

def numberPower(num1, num2):
    return num1**num2
numberPower(2,2)

int1 = 4
int2 = 3

def numPow(int1, int2):
    powerResult = int1 ** int2
    print(powerResult)
    return powerResult
numPow(int1, int2)

# #2.3. Tax function (3 points)
# Rewrite the code from HW2 (exercise 2.7) into a function. The function shall take 
# the price of the item as an argument and return the price with tax.


def priceItem(item):
    taxPrice = item * 0.07
    totalPrice = item + taxPrice
    print(f"Tax on this item is 0.07 ; The total price is: ${format(totalPrice, '.2f')}")
priceItem(float(input(" Please, enter an item price: ")))

def taxFunction(price):
    tax = price * .07
    total = price + tax
    total = format(total, ".2f")
    return total
itemPrice = float(input("Enter an item price:"))
result = taxFunction(itemPrice)
print(f"Total price with tax is : ${result}")

 

# #2.4. Average function (3 points)
# Write a function that takes three arguments (numerical) and returns the average 
# of the numbers entered.

def average(num1, num2, num3):
    return (num1 + num2 + num3)/3
average(3,6,9)
