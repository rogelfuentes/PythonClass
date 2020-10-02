print('Hello'.center(20, '='))

print("The {} {} {}".format("Fox","Brown", "Quick"))

# Index name
print("The {2} {1} {0}".format("Fox","Brown", "Quick"))

# Key name
print("The {f} {q} {f}".format(f = "Fox", b = "Brown", q = "Quick"))

# Float format {value:width.precision f}
result = 100/777
print(result)
print("The result was {r:1.3f}".format(r=result))
print("The result was {r:10.3f}".format(r=result))

name = "rogel"
age = 20
print(f"Hello, my name is {name.title()}, my age is {age}")
