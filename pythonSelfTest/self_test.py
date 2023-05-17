import sys


def choise():
    print("Question 1:")
    print("Question 2:")
    print("Question 3:")
    print("Question 4:")
    print("Question 5:")
def main():
    choise()
    while True:
        value = input("Choose between 1 to 5 or X to close the program: ")
        if value == "X"  or value== "x":
            print("Program Closed")
            sys.exit()
        elif value == "1":
            n = int(input('Table of '))
            for i in range(1,11):
                print(n, "x", i , "=", i*n)
        elif value == "2":
            n = int(input("Factorial of: "))
            fact = 1
            for i in range (1,n+1):
                fact *= i
                print(fact)
        else:
            print("Wrong input!")
            print("Choose between 1 to 5 or X to close the program") 
if __name__ == "__main__":
    main()


