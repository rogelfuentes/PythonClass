filePath = 'files/pi_digits.txt'

with open(filePath) as file_object:
    contents = file_object.read()
print(contents.rstrip())

# .rstrip() = To remove the extra blank line

# File reader

filePath = 'files/pi_digits.txt'

with open(filePath) as file_object:
    for line in file_object:
        print(line)

# It liminates the empty lines by using (.rstrip()) 
with open(filePath) as file_object:
    for line in file_object:
        print(line.rstrip())

# Working with file content
with open(filePath) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.rstrip()

print(pi_string)
print(len(pi_string))

#--------

with open(filePath) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(pi_string)
print(len(pi_string))

# -------------

with open(filePath) as file_object:
    lines = file_object.readlines()

pi_string = ''

for line in lines:
    pi_string += line.strip()

print(f"{pi_string[:10]}")
print(len(pi_string))