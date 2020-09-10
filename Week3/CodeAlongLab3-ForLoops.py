# For Loops

fruit = "apples"
for c in fruit:
    print(c)
print("done")

total = 0
for i in range(10000):
    # total = total + i
    total += i
print("Sum of all numbers from 0 to 10000:", total)

characters = ["Thor", "Thanos", "Black Panter", "Iroman", "Hulk", "Batman", "Captain America"]
for i in characters:
    print(i)

# Use this line of code and write a for loop to iterate and print each name in the variable.
sharks = ['hammerhead', 'great white', 'dogfish', 'frilled', 'bullhead', 'requiem']
for i in sharks:
    print(i)

# Expected output:
# hammerhead
# great white
# dogfish
# frilled
# bullhead
# requiem