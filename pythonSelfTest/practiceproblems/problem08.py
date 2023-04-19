"""
A student will not be allowed to sit in exam if his/her attendance is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
"""
numberOfClasses = int(input('How many total have been taken: '))
numberOfAttendend = int(input("Student attended class: "))
percentage = (numberOfAttendend * 100) / numberOfClasses
print(percentage,"% attended")

ask = input("Do you have any medical condition? ")

if ask == 'y' or ask == 'Y':
    print("You can sit for exam with special permission")
elif ask == 'n' or ask == 'N':
    if percentage < 75:
        print("Not allowed to sit for exam")
    else:
        print("You can sit for exam")
elif percentage > 100:
    print("Percentage can't be above 100%")
else:
    print("Invalid input. Please enter 'y' or 'n'.")



