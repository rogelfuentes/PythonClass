#  Simple For loop
prices = [1.2, 3.5, 5.2]
for p in prices:
    print (p, p * 0.07)

# While loop
prices = [1.2, 3.5, 5.2]
counter = 0

while counter < 3:
    prices[counter] = prices[counter] * 1.07
    counter += 1
print[prices]

# or 
while counter < len(prices):
    prices[counter] = prices[counter] * 1.07
    counter += 1
print[prices]

#  For loop
prices = [1,2,3,4,5,6]

for i in range(len(prices)):
    prices[i] *= 1.07
print(prices)
