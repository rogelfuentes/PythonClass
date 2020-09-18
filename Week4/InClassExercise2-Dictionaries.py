# 1.1 Create Dictionaries (2.5 points)
# Use any names and birthdays you want to create a birthday dictionary that has four entries.  
# The name is the key and the value is the birth date.  Print each birth date by using the key to access each entry.  

birthDict = {
    "Carlos": "Apr, 26, 2001",
    "Luis": "May, 13, 1945",
    "Mary": "Dec, 01, 1980",
    "Wendy": "Jul, 12, 2015"
}
for key in birthDict.items():
    print(key)

name = birthDict["Carlos"]
print(name)
name = birthDict["Luis"]
print(name)
name = birthDict["Mary"]
print(name)
name = birthDict["Wendy"]
print(name)

# #1.2 Update Dictionaries (2.5 points)
# Using the dictionary from above, update the last entry and change the birth date to 06/06/1980.

birthDict["Wendy"] = "Aug, 20, 2016"
print(birthDict["Wendy"])


# #1.3 Dictionary With Lists (2.5 points)
# Create a dictionary of the seasons Fall, Spring and Summer where the name of the season is the key and 
# the value is a list of the months in that season. Print the value of "Fall".

seasons = {
    "Fall": ["Sept", "Oct", "Nov"],
    "Spring": ["Mar", "Apr", "May"],
    "Summer": ["Jun", "Jul", "Aug"],
}
print(seasons["Fall"])

for season in seasons:
    if season == "Fall":
        item = seasons[season]
        print(item)


# #1.4 Dictionary Merge (2.5 points)
# Create the same dictionary as in exercise 3 but also create a second dictionary with only the season of Winter.  
# Use the dictionary.update method to merge the winter dictionary into the seasons dictionary.  Print the seasons dictionary.

winter = {
    "Winter": ["Dec", "Jan", "Feb"]
}

seasons.update(winter)
print(seasons)