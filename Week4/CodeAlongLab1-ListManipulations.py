prices = [1.10, 0.99, 5,75]


for itemPrice in prices:
    print("Original price:", itemPrice)
    itemPrice *= 1.07
print("Orignal prices:", prices)


i = 0
for itemPrice in prices:
    prices[i] *= 1.07
    prices[i] = format(prices[i], ".2f")
    i += 1 
print(prices)  


position = 0
while position < len(prices):
    prices[position] *= 1.07
    prices[position] = format(prices[position], ".2f")
    position += 1
print(prices) 



myNumbers = "10,20,30,40,50,60"
print(myNumbers)
numberList = myNumbers.split(",")
print(type(numberList))
print(len(numberList))



myString = "apples, bananas, oranges"
stringList = myString.split(",")
print(stringList)



myTime = "10:05:45,09:45:32,07:30:25"
timeList = myTime.split(",")
for item in timeList:
    time = item.split(":")
    print(time)


time = "07:49:34"
hrs, mins, sec = time.split(":")
print (hrs, mins, sec)

