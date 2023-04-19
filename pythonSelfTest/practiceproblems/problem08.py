"""
A student will not be allowed to sit in exam if his/her attendance is less than 75%.
Take following input from user
Number of classes held
Number of classes attended.
And print
percentage of class attended
Is student is allowed to sit in exam or not.
"""
numberOfClasses = int(input('How many total have been taken:  '))
numberOfAttendend = int(input("Student attended class: "))
percentage = (numberOfAttendend * 100) / numberOfClasses
print(percentage,"% attendend")
if percentage < 75 :
    print("Not allow to sit for exam")
elif percentage > 100:
    print("Parcentage cant be above 100%")
else:
    print("You can sit for exam")
