#practchng on 10.02.2023 12.43AM
import sys
def printOptions():
    print("1.Print 1 to N")
    print("2.Print 1 to N(sum)")
    print("3.Print table")
    print("4.Print reverse array ")
    print("5.Print factorial of N ")
    print("6.Exit ")

def main():
    while True:
        printOptions
        option = int(input("Enter your choise__ "))
        
        if option == 1:
            n = int(input("N: "))
            for i in range(n):
                print(i+1)
        elif option == 2:
            n = int(input("N: "))
            sum = 0
            for i in range(n):
                sum += 1 + i
                print(sum)
        elif option == 3:
            n = int(input("N: "))
            for i in range(1,11):
                print(n ,"X", i , "=", i*n)
        elif option == 4:
            str = input("Input your string: ")
            s = ""
            for char in str:
                s = char + s
                print(s)
        elif option == 5:
            n = int(input("N: "))
            fact = 1
            for i in range(1 ,n+1):
                fact *= i
                print(fact)
        elif option == 6:
            print("Exited")
            sys.exit()
        else:
            print("Wrong input, select again")
            
if __name__ == "__main__":
    main()