myDict = {
    "name":"Thor",
    "age": "1500",
}
print(myDict)

exampleDict = {
    "animals":["Dogs", "Cats", "Fish", "Tigers"],
    "numbers":1,
    "name": "Carlos",
    "boolean": True,
    "another Dict":{
        "you could": "keep going",
        "like this": "for ever"
    }
}
for key in exampleDict:
    print(key)

for key in exampleDict.keys():
    print(key)

for item in exampleDict.items():
    print(item)

seasons = {
    "Fall": ["Sept", "Oct", "Nov"],
    "Spring": ["Mar", "Apr", "May"],
    "Summer": ["Jun", "Jul", "Aug"],
}
print(seasons)

winter = {
    "Winter": ["Dec", "Jan", "Feb"]
}

seasons.update(winter)
print(seasons)


for key, value in seasons.items():
    print(key + ":", value)


# Sets demo
smallPrimes = set()
smallPrimes.add(2)
smallPrimes.add(3)
smallPrimes.add(5)
print(smallPrimes)
smallPrimes.add(1)
smallPrimes.add(1)
smallPrimes.remote(1)
print(smallPrimes)

# tuples
t = ("a", "b", "c", "e")
print(t)
print(type(t))
t[1] = "xyz"

