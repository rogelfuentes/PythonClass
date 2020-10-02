x = 126864.5546739
y = 468883076449009
formatted = format(x, ".2f")
formatted2 = format(x, ",.2f")
formatted3 = format(y, ",d")
print (x, type(x))
print (formatted, type(formatted))
print (formatted2, type(formatted2))
print (formatted3)


print ("Name", "Department")
print ("Juberth", "Information Systems")

w1 = "Name"
w2 = "Department"
w3 = "Juberth"
w4 = "Information Systems"

ab1 = format(w1, "10s")
ab2 = format(w2, "10s")
ab3 = format(w3, "15s")
ab4 = format(w4, "15s")

print(ab1, ab3)
print(ab2, ab4)

ab1 = format(w1, ">10s")
ab2 = format(w2, ">10s")
ab3 = format(w3, ">20s")
ab4 = format(w4, ">20s")

print(ab1, ab3)
print(ab2, ab4)