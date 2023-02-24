import sys


def menu():
    print("1. Print 1 to N")
def main():
    menu()
    while True:
        choice = input("Choobse between [1-6] or X to Exit: ")
        if choice == "X" or choice == "x":
            print("Program Closed")
            sys.exit()
        elif choice == "1":
            n = int(input("N: "))
            for i in range(n+1):
                print(i)
        elif choice == "2":
            n = int(input("N: "))
            sum = 0
            for i in range(n):
                sum += i + 1
                print(sum)
        else:
            print("Choose between [1-6]")

if __name__ == "__main__":
    main()
            