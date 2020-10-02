numberOfScores = int(input("Enter how namy scores: "))

scores = []
for x in range (0, numberOfScores):
    while True:
        try:
            score = int(input("What is the score #: " + str(x+1)))
        except:
            print("Invalid score value. Please try again.")
        else:
            break

try:
    print(sum(scores/numberOfScores))
except ValueError:
    print("You enters the wrong value")
except TypeError:
    print("Opps, you entered a string not a number.")
except:
    print("An unknown error has occured")




while True:
    try:
        emailAddress = input("Enter an email address: ")
        parts = emailAddress.split("@")
        name = parts[0]
        domain = parts[1].split(".")
        print("The email address is: ", name, domain[0], domain[1])
        print("Thank you")
        break
    except:
        print("Not a valid email address, please try again.")
