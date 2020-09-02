# Exercise 5: hours-minutes (2 points)

# Create two variables to hold values for a pay rate and minutes worked.
# Create another variable to convert the amount of minutes to hours.
# Create a results variable to calculate the hours and the pay rate.
# Assign pay rate = 18 and minutes = 470.
# Using the print function, display the pay results with a dollar sign in front of the value. (eg, $126)


payRate = 18
minutes = 470

cHours = minutes / 60
totalPay = str(payRate * cHours)

print("The total pay for " + str(round(cHours,2)) + " hours is $" + totalPay )

