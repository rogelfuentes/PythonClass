# #1. Exception handling (5 points)
# Write a loop that uses a try except else block to verify that the user entered a valid number.  
# The loop should run until a valid number has been entered.

while True:
    try:
       validNumber = int(input("Enter a valid number (Integer)"))
    except:
        print("That is not a valid number")
    else:
        print("You entered a valid number")
        break


# #2. File IO (5 points)
# Write a program that opens a file that will be overwritten each time.  Write out a few lines of text and then close the file.

fileOut = open("text.txt", "w")
fileOut.write("Hello\n")
fileOut.write("World")
fileOut.close()


# #3. Name (5 points)
# Write a program that prompts the user for a file name.  If the file exists, open it and print each line.  
# If the file does not exist, handle the open file exception and print a message stating that the file was not found.

fileName = input("Enter a file name: ")
try:
    fileIn = open(fileName, 'r')
    for line in fileIn:
        print(line)
    fileIn.close()
except:
    print("File not fount")
