# Exercise #1: (10 points)
# Fantasy Game Inventory
# You are creating a fantasy video game. The data structure to model the player’s inventory will 
# be a dictionary where the keys are string values describing the item in the inventory and the 
# value is an integer value detailing how many of that item the player has. For example, the 
# dictionary value {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12} means the 
# player has 1 rope, 6 torches, 42 gold coins, and so on. Write a 'for loop' and print out the 
# players inventory. The output should be as below:

# Inventory:
# 1 rope
# 6 torch
# 42 gold coin
# 1 dagger
# 12 arrow
# 3 map fragments
# Total number of items : 65
# Hint: You can use a for loop to loop through all the keys in a dictionary. Use the dictionary below:

stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12, 'map fragments' : 3 }

totalItems = 0
print("Invertory:\n")
for item in stuff:
    print(f"{stuff[item]}" + " " + f"{item}\n")
    totalItems += stuff[item] 
print(f"Total number of items: ", totalItems)



# Exercise #2: (10 points)
# Comma Code
# Say you have a list value like this:
# characters = ["Thor", "Thanos", "Black Panther", "Iron Man", "Hulk", "Batman", "Captain America"]
# Write Python code that coverts the list into a string with all the items separated by a comma and a 
# space, with 'and' inserted before the last item. For example, converting the characters list look like this:
# 'Thor, Thanos, Black Panther, Iron Man, Hulk, Batman and Captain America.'
 

characters = ["Thor", "Thanos", "Black Panther", "Iron Man", "Hulk", "Batman", "Captain America"]


for character in characters:
    if character == characters[-1]:
        print(f"and {character}.")
    elif character == characters[-2]:
        print(character, end = " ")
    else:
        print(f"{character}, ", end =" ")





# Exercise #3: (10 points)
# Create a dictionary of technical terms and allow the user to lookup the definitions of these terms from the dictionary. 
# Use the following list for your dictionary:
# 'dict', 'list', 'map', or 'set'


# You can use the following resource:
# dict = “stores a key/value pair”
# list = “stores a value at each index”
# map = “see dict”
# set = “stores unordered unique elements”


# Based on the user's input, print the term and the definition.
# Make “exit” a term in the dictionary. Prompt the user to enter a term inside a while loop until the user types the word “exit”.

dictionary = {
    'dict':'stores a key/value pair', 
    'list':'stores a value at each index', 
    'map' : 'see dict', 
    'set' : 'stores unordered unique elements'}


exit = True

while exit:
    word = (input(f"Type the word to find the definition 'dict,list,map, set or type 'end' to finish the program: "))
    if word == "end": 
        exit = False
    else: 
        print(f"{word}:" + dictionary.get(word))
        exit = True
print("Finished")
