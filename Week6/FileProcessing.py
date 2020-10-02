# Using open()
# handle = open(filename, mode)
# mode is optional and should be 'r' if we are planning to
# read the file and 'w' if we are going to write to the file

fhand = open('files/text.txt', 'r')
print(fhand)

# File Handle as a Sequence

xfile = open('files/text.txt')
for cheese in xfile:
    print(cheese)

textFile = open('files/testscores.txt')
count = 0
for line in textFile:
    count = count + 1
print('Line Count:', count)

# Reading the *Whole* File
fhand = open('files/text.txt')
inp = fhand.read()
print(len(inp))
print(inp[:20])

# Searching Throgh a file (It is case sensitive)
fhand = open('files/text.txt')
for line in fhand:
    if line.startswith('Wo') :
        print(line)

# Skipping with continue (We can conveniently skip a line by using the continue statement)
fhand = open('files/pi_digits.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('897') :
        continue
    print(line)

# Prompt for file name
fname = input('Enter the file name: ')
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)


# Bad File Names
fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
quit()
count = 0
for line in fhand:
    if line.startswith('Subject:') :
        count = count + 1
print('There were', count, 'subject lines in', fname)