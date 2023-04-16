"""
Take input of age of 3 people by user and determine oldest and youngest among
them.
"""
name1 = input("Person 01 ?")
name2= input("Person 02 ?")
name3 = input("Person 03 ?")
age1 = int(input("Age of {}? ".format(name1)))
age2 = int(input("Age of {}? ".format(name2)))
age3 = int(input("Age of {}? ".format(name2)))
if age1 > age2 and age1 > age3:
    print(name1,"is the oldes of them.")
elif age2 > age3 and age2 > age1:
    print(name2,"is the oldest one.")
else:
    print(name3,"is the oldest one.")

if age1 < age2 and age1 < age3:
    print(name1,"is the youngest of them.")
elif age2 < age3 and age2 < age1:
    print(name2,"is the youngest one.")
else:
    print(name3,"is the youngest one.")