import sys
def cho():
    print("1. Print 1 to N")

def main():
    cho()
    while True:
        choise = input("Chooose between [1 - X], X to close the program: ")
        if choise == "1":
            n = int(input("N: "))
            for i in range(n+1):
                print(i)
        elif choise == "x" or choise == "X":
            print("Program Closed")
            sys.exit()
        else:
            print("Wrong input, choose between [1-x]")

if __name__ == "__main__":
    main()