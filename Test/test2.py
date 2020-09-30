my_var = 15

if int(my_var) >= 20:
    print('too high')

elif int(my_var) >= 18 and my_var < 20:
    print('too low')
else:
    print('undefined parameter')


numbers = [[1,2,3],[4,5,6],[7,8,9]]
print(numbers[0])

s = "python rocks"
print(s[2] + s[-4])

alist = [3, 67, "cat", [56, 57, "dog"], [ ], 3.14, False]
print(alist[5])

print(18 / 4)
print(18 % 4)

16 - 2 * 5 // 3 + 1

x = 15
y = x
x = 22
print(x,y)

x = 12
x = x - 3
x = x + 5
x = x + 1
print(x)

L = [0.34, '6', 'SI106', 'Python', -2]
print(len(L[1:-1]))

s = "python rocks"
print(s[3:8])

alist = [1,3,5]
blist = [2,4,6]
print(alist + blist)

qu = "wow, welcome week!"
ty = qu.index("we")
print(ty)

qu = "wow, welcome week! Were you wanting to go?"
ty = qu.count("we")

let = "z"
let_two = "p"
c = let_two + let
m = c*5
print(m)

ls = ['run', 'world', 'travel', 'lights', 'moon', 'baseball', 'sea']
new = ls[2:4]
print(new)

s = "python rocks"
for ch in s[3:8]:
   print("HELLO")

   p = [3, 4, "Me", 3, [], "Why", 0, "Tell", 9.3]
for ch in p:
   print(ch)

if (4 + 5 == 10):
    print("TRUE")
else:
    print("FALSE")
print("TRUE")

mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
yourdict = mydict
yourdict["elephant"] = 999
print(mydict["elephant"])


def print_many(x, y):
       """Print out string x, y times."""
for i in range(y):
       print(x)

z = 3

print_many("Greetings", z)

def addEm(x, y, z):
    return x+y+z
    print('the answer is', x+y+z)