# def print_menu():
#     print("1. Print 1 to n")
#     print("2. Print sum of n")
#     print("3. Print multplication table")
#     print("4. Print reverse string")
#     print("5. Print factorial of n")

# def main():
#         while True:
#             print_menu()
#             choise = int(input("Enter your choie [1-5]: "))

#             if choise == 1:
#                 n = int(input("N" ))
#                 for i in range(n):
#                     print(i)
#             elif choise == 2:
#                 n  = int(input("N: "))
#                 sum = 0
#                 for i in range(n):
#                     sum += i + 1
#                     print(sum)
#             elif choise == 3:
#                 n = int(input("N"))
#                 for i in range(1,11):
#                     print(i , "X", n , "=", n*i)
#             elif choise == 4:
#                 str = input("Give a string: ")
#                 s = ""
#                 for char in str:
#                     s = char + s
#                     print(s)
#             elif choise == 5:
#                 n = int(input("N: "))
#                 for i in range(1, n+1):
#                     fact = 1
#                     fact *= i
#                     print(fact)
#             else:
#                 print("Wrong input!!")

# if __name__ == "__main__":
#     main()
            

import sys


def print_menu():
    print("1. Print 1 to n")
    print("2. Print sum of n")
    print("3. Print multiplication table")
    print("4. Print reverse string")
    print("5. Print factorial of n")

def main():
    while True:
        print_menu()
        choice = int(input("Enter your choice [1-5]: "))

        if choice == 1:
            n = int(input("N: "))
            for i in range(n):
                print(i)
        elif choice == 2:
            n = int(input("N: "))
            s = 0
            for i in range(n):
                s += i + 1
                print(s)
        elif choice == 3:
            n = int(input("N: "))
            for i in range(1, 11):
                print(i, "X", n, "=", n*i)
        elif choice == 4:
            string = input("Give a string: ")
            s = ""
            for char in string:
                s = char + s
                print(s)
            sys.exit()
        elif choice == 5:
            n = int(input("N: "))
            fact = 1
            for i in range(1, n+1):
                fact *= i
                print(fact)
            sys.exit()
        else:
            print("Wrong input!!")
            sys.exit()

if __name__ == "__main__":
    main()
