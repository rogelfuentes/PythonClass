# #1.1. Hello World (again) (3 points)
# Write a function that asks for the user’s name and prints “Hello, “ followed by their name.

def hello():
    userName = input("What is your name: ")
    print("Hello " + userName)
hello()

 
# #1.2. Dog Years (3 points)
# Write a function that asks for the age of the user’s dog. Print a string that states the dog’s age in dog years with a conversion rate of 1 human year to 7 dog years.

def dogAge():
    UdogAge = int(input("What is your dog age? "))
    UdogAgeT = UdogAge * 7
    print(f"Your dog has {UdogAgeT} of human age")
dogAge() 

def calDogYears():
    age = input("How old is your Dog?")
    print("Your dog is" + str(int(age*7)) + "in human years")
calDogYears()

 

# #1.3. Purchase (3 points)
# Write a function that asks for the user to enter a number of items they wish to purchase.

def items():
    purchaseItems = int(input("Hoe many items do you want to purchase? "))
    print(purchaseItems)
items()

def purchase():
    items = input("How many items do you want to purchase?")
    print(items)