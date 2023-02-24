import time
print("Press Y to continue")
menu = ('Y','y')
check = input("Y/N \n")
while check in menu:
    print("Loading.")
    time.sleep(1)
    print("Loading..")
    time.sleep(1)
    print("Loading...")
    time.sleep(1)
    print("Loading....")
    time.sleep(1)
    print("Loading.....")
    time.sleep(1)
    
    print("What is your name and age ?")
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    curretYear = 2023
    yourBirthyear = 2023 - age
    print(yourBirthyear)
else:
    print("Exited")
