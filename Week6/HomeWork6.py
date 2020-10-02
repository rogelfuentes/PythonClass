# Exercise #1: (6 points)
# Write a Python program that asks the user to type in a word in English. Determine if 
# that name is one of the most 100 popular English words. Download and use the data file 
# in Canvas called most_popular_words_in_english.txt located in Module 5 and the Files section.
# Link to required file:

 
# Here's how to get started:
# Read in the data and print it out (use the sample code below to get started).
# Next, split the data using the correct separator character (hint: there is a line break between each word).
# Finally, use the appropriate built-in functions and list methods to determine if the user's word is contained in the list that you generated in the previous step.


# Sample code, use this to help get you started:
# try:
#     # open a file for reading
#     myvar = open("most_popular_words_in_english.txt", "r")

# # an error occurred!  handle it here
# except:
#     print ("Something went wrong!")



while True:
    try:
        # asks the user to type in a word in English.
        userWord = input("Type a common word in English: ")

        if  userWord.isalpha():
            # Determine if that name is one of the most 100 popular English words.
            filePath = "files/most_popular_words_in_english.txt"
            with open(filePath) as fileObject:
                content = fileObject.read()
                if userWord in content:
                    print(f" \"{userWord}\" is one of the most popular words in English")
                    break
                else:
                    print(f"\"{userWord}\" is not in the list.")
                    break        
    except:
        print("That's no a valid word, try again")


 

# Exercise #2: (6 points)
# Write a security program that prompts the user for a username and a password. 
# Store the username and password into a file named "security.txt" - make sure 
# to store the username and password on separate lines.


userName = input("Enter the username: ") 
file = open("files/security.txt", 'a')
file.write(userName + "\n")
password = input("Enter the password: ") 
file = open("files/security.txt", 'a')
file.write(password + "\n")
file.close()



# Exercise #3: (6 points)
# Write a program that opens the "security.txt" file you created for the previous programming 
# exercise and read in the username and password stored in the file. Store these values into 
# a series of variables. Next, prompt the user for a username and password using the input function. 
# If the values supplied by the user match the values stored in the file, allow them to continue. 
# Otherwise present an error message.

# Open the file
fileObject = open("files/security.txt", "r")

# Pull the data from the file
alldata = fileObject.read()

# Close the file
fileObject.close()

#  split the string
splitdata = alldata.split("\n")

# New variables for the data
username = splitdata[0]
password = splitdata[1]

# Request username and password fron the user
typeUserName = input("Type your username: ")
typePassword = input("Type your password: ")

# Comparing data
if username == typeUserName and password == typePassword:
    print("Access Granted")
else:
    print("Password or username are incorrect")



# Exercise #4: (6 points)
# Write a program that opens up a file named "testscores.txt" (available in Canvas under Module 5 
# or in the Files section). This file contains the following information in the following format:
# student name
# score1
# score2
# score3
# Read in the values and print out the average score for the student specified in the file along
#  with the student’s name.

# Open the file
fileObject = open("files/testscores.txt", "r")
# Read the data
alldata = fileObject.read()
# Split data
splitData = alldata.split("\n")

# Assing a variable for each data
studentName = splitData[0]
score1 = splitData[1]
score2 = splitData[2]
score3 = splitData[3]

# Calculate the average
average = (int(score1) + int(score2) + int(score3))/3
print(f"The student {studentName} has an average of: {average} ")