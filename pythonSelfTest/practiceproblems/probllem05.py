"""
A school has following rules for grading system:
a. Below 25 - F
b. 25 to 45 - E
c. 46 to 50 - D
d. 51 to 60 - C
e. 61 to 80 - B
f. Above 80 - A
Ask user to enter marks and print the corresponding grade.
"""
sub = input("Subject name:")

print("Your marks in",sub,"? - ")
marks = float(input())
if marks < 25:
    print("Grade: F")
elif marks <= 45:
    print("Grade: E")
elif marks <= 50:
    print("Grade: D")
elif marks <= 60:
    print("Grade: C")
elif marks <= 80:
    print("Grade: B")
else:
    print("Grade: A")
