# Write with Quotes
print(" \"Double Quote\", \'Single Quote\', \\BackSlash, \nNew Line!, \tTab  ")

# Secuence & Iterables
myString = "Hey good morning my friend!"
for eachCharacter in myString:
    print(eachCharacter)

# Reading & Converting
name = input('Enter:')
print(name)
apple = input("Enter a number:")
print(int(apple) - 10)

# Looking Inside String
fruit = "Banana"
singleLetter = fruit[1]
print(singleLetter)

# len()
fruit = "Banana"
print(len(fruit))

# String Library
upperCase = "Hellow World"
message = upperCase.upper()
print(upperCase.upper())
print(message)
print("Hey There!".lower())
print(type(upperCase))
print(dir(upperCase))

# String Methods
s = "Caramba   "
print(s.index('a'))
print(s.count('a'))
print(s.strip('a'))

# find() Searching a String
fruit = "Banana"
finding = fruit.find('Ba')
print(finding)

# Making everything UPPER\lower CASE

x = "Venezuela"
y = "UPPER CASE"
print(x.upper())
print(x.lower())
print(y.isupper())
print(y.islower())

# Search and Replace: .replace()
greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)
nstr = greet.replace('o', 'X')
print(nstr)


# Removing White Space .strip() - lstrip() - rstrip()
greet = '  Hello Bob  '
nstr = greet.strip() 
nstr = greet.rstrip()
nstr = greet.lstrip()
print(nstr)

# .format() - String Formatting
myName = "rogel"
print("Hey " + myName)
print(f"This is a f-String formating, my name is {myName.title()} ")

txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))



#  isX string methods, all are boolean
A = " Tomatoes "
print(A.isalpha()) 
print(A.isalnum()) 
print(A.isdecimal()) 
print(A.isspace()) 
print(A.istitle()) 

while True:
    print(("Enter your age:"))
    age = input()
    if age.isdecimal():
        print("Good job, thanks!")
        break
    print("Please enter a number for your age")


# startswith() & endswith()
'Hello world!'.startswith('Hello') 
'Hello world!'.endswith('world!')
'abc123'.startswith('abcdef')
'abc123'.endswith('12')

# join() Method
print(", ".join(["cats", "dogs", "fish"]))
print("ABC".join(["My", "name", "is", "John"]))


# Justifying Text
# rjust() – Right justify
# ljust() – Left justify
# center() – Center justify

'Hello'.center(20)
'Hello'.center(20, "=")
'Hello'.rjust(20)
'Hello'.rjust(20, "=")
'Hello'.ljust(20)
'Hello'.ljust(20, "=")