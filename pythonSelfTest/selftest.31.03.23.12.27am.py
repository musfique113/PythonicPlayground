import sys
def choisex():
    print("Q1")
    print("Q2")
    print("Q3")
    print("Q4")
    print("Q5")
    print("Q6")
def main():
    choisex()
    while True:
        choise = input("Enter your choise bewteen 1 to 6 , or X to close the program.")
        if choise == "1":
            n = int(input("N: "))
            for i in range(n+1):
                print(i)
        elif choise == "x" or choise == "X":
            print("Program Closed")
            sys.exit()
        else :
            print("Wrong Input")

if __name__ == "__main__":
    main()
