def yesNoBooleanConverter(val):
    val = str(val).upper()
    if val == "Y" or val == "YES":
        return True
    else:
        return False

def booleanYesNoConverter(val):
    if val :
        return "Yes"
    else:
        return "No"

def moveQueueValueConverter(value):
    val = str(value).upper()
    if val == "R":
        return "Released"
    elif val == "H":
        return "Hold"
    elif val == "D":
        return "Delete"
    elif val == "P":
        return "Pending"
    else: 
        return None

def NullToBooleanConvert(value):
    return value != None

def CToF(value):
    fahrenheit = (value * 9/5) + 32
    return fahrenheit

def FToC(value):
    celsius = (value - 32) * 5/9
    return celsius


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
    
    # In the ICE1.py script, use the random generator and generate a number between 1 and 9. Pass the number into the getAnswer() function and print out the users fortune.

