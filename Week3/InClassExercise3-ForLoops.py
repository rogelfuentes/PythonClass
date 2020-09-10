# In-class exercise 3 - for loops

# #1 Input with a for-loop (4.5 points)
# Asks the user for how many numbers they want to add.  Reads in each number and prints a total at the end.
# Hint: use the range() function: for i in range(quantity):

totalNum = int(input("How many numbers do you want to add? :"))
totalAddNum = 0
for i in range(totalNum): 
    addNum = float(input("what is the number to add?: "))
    totalAddNum += addNum
print(f"The total sum that you has been adding is: {totalAddNum}")


# #2 Find the vowels – for loop (4.5 points)
# Using the 'if' statement and the 'or' operator, write a program that uses the input() function and asks the user for a word or sentence.
# Print the number of vowels in the string that’s returned from the input() function.
# Use the 'or' operator inside the 'if' condition.

# Pseudo code:
# Prompt user for a word or phrase.
wordPhrase = str(input("Type a word or a phrase: "))
total = 0
vowelList = []

# enter 'for' loop:
for i in wordPhrase:
# for each letter, check if the letter is an 'a,e,i,o or u'.
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
# If a match, then +1 to total.
        total += 1
        vowelList.append(i)
# end loop.

# Print total results.
print(total)
print(f"The vowels in the list are:{vowelList}")
