import sys
def menu():
    print("1. Print 1 to N")
    print("2. Print sum of 1 to N")
    print("3. Table")
    print("4. Revere ARRAY")
    print("5. FActorial of N")
    print("6. Fiboonacci serise")
    print("X. Close program")
def main():
    menu()
    while True:
        choise = input("Choose between 1 to 6 or X to close the program: ")
        if choise == "1":
            n = int(input("N: "))
            for i in range(n+1):
                print(i)
        elif choise == "x" and choise == "X":
            print("Program closed")
            sys.exit()
        elif choise == "2":
            n = int(input("N: "))
            sum = 0
            for i in range(n):
                sum += i + 1
                print(sum)
        elif choise == "3":
            n  = int(input("Table of "))
            for i in range(1,11):
                print(n,"X",i,"=",i*n)
        elif choise == "4":
            str = input("Ehter sting: ")
            s = ""
            for char in str:
                s = char + s
                print(s)
 
        else:
            print("Wrong input!!")
if __name__ == "__main__":
    main()
    
