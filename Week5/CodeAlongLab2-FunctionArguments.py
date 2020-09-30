

def format_name(first_name, last_name):
    return first_name + " " + last_name
first = input("What is your full name?")
last = input("What is your last name?")
print("Hello", format_name(first, last))



def average(num1, num2, num3):
    sum = num1 + num2 + num3
    avg = sum/3
    print(avg)
average(3,18,25)


def func(num1, num2):
    if num1 < 0:
        return
    else:
        retval = num1 + num2 
        return retval
        # or 
        # return num1 + num2
print(func(-1, 20))


def printDict(dictionary):
    keys = list(dictionary.keys())
    values = list(dictionary.values())
    for i in range (0,len(keys)):
        k = keys[i]
        v = values[i]
        print(k,v)

exampleDict = {
    "name": "Thor",
    "age": "25"
}

printDict(exampleDict)

def sumTwoNumbers(a,b):
    return a + b

num1 = int(input("Enter a number:"))
num2 = int(input("Enter another number:"))
print(sumTwoNumbers(num1, num2))




def multiplyBy (a, b=2):
    return a * b
print(multiplyBy(2,3))
print(multiplyBy(2))



def func(*args):
    print(args)
func(1,2,3,4,5,6,7,8,9,10)




def func(**kwargs):
    print(kwargs)
func(a=1, b=2, c=3)



def dbConnect(**options):
    connString = {
        "host":options.get("host", "127.0.0.1"),
        "port":options.get("port", 5432),
        "user":options.get("user", "admin"),
        "pwd": options.get("pwd", ""),
        "catalog": options.get("catalog", "defaultName")
    }
    print(connString)

    dbConnect (host = "192.0.0.1", port=12202, user="Admin", pwd="gandalf",catalog="testt" )
