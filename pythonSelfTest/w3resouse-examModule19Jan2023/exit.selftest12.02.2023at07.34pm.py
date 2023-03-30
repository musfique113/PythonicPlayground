import sys


def menu():
    print("1. Print 1 to N")
    print("2. Print aum of 1 to N")
    print("3. Table")
    print("4. Revere ARRAY")
    print("5. FActorial of N")
    print("6. Fiboonacci serise")
    print("X. Close program")


def main():
    menu()
    while True:
        choise = input(
            "Choose between [1 - 6], or enter 'x' to exit: ").lower()
        if choise == "1":
            n = int(input("N: "))
            for i in range(n):
                print(i+1)
        elif choise == "X" or choise == "x":
            print("Closed")
            sys.exit()
        elif choise == "2":
            n = int(input("N: "))
            s = 0
            for i in range(n):
                s += i + 1
                print(s)
        elif choise == "3":
            n = int(input("Table of: "))
            for i in range(1, 11):
                print(n, "X", i, "=", i*n)
        elif choise == "5":
            n = int(input("Factorial of: "))
            fact = 1
            for i in range(1, n+1):
                fact *= i
                print(fact)
        elif choise == "4":
            str = input("Input STRING: ")
            s = ""
            for char in str:
                s = char + s
                print(s)
        elif choise == "6":
            n = int(input("Enter the number of terms: "))
            a, b = 0, 1
            print("Fibonacci series:")
            for i in range(n):
                print(a)
                a, b = b, a + b
        else:
            print("Wrong input!!\nChoose between [1-6]")

if __name__ == "__main__":
    main()

    
