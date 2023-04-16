# A company decided to give bonus of 5% to employee if his/her year of service is more than 5 years. Ask user for their salary and year of service and print the net bonus amount.

print("Welcome, Please give some inforation. \n")
name = input("Enter your name: ")
presentSalary = int(input("Your presnt salary? - "))
expericence = int(input("How many years are you in service? - "))
hike = 0.05
if expericence >= 5:
    bonusOnSanalry = presentSalary*hike
    print("You salary with bonus:",bonusOnSanalry+presentSalary)
else :
    print(name,"Sorry, You are not eligible for salary.")