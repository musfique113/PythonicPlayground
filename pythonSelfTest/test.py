import sys
def choise():
    print("Chooise between [1-10] or X to close the program: ")

def main():
    choise()
    while True:
        opt = input("Your choise: ")
        if opt == "1":
            n = int(input("Print 1 to n, n = : "))
            for i in range (n+1):
                print(i)

        elif opt == "X" or opt == "x": # "or" not "and"
            print("Exited")
            sys.exit()
        
        elif opt == "4":
            str = input("Input your string: ")
            s = ""
            for char in str:
                s = char + s
                print(s)

        elif opt == "2":
            n = int(input("Table of : "))
            for i in range(1,11):
                print(i, "x" , n , "=", i*n)

        elif opt == "3":
            n = int(input("Factorial of: "))
            fact = 1
            for i in range(1, n+1):
                fact *= i
                print(fact)  
        elif opt == "5":
            n = int(input("N: "))
            fact = 1
            for i in range(1 ,n+1):
                fact *= i
                print(fact) 

        elif opt == "6":
            n = int(input("N: "))
            sum = 0
            for i in range(n):
                sum += 1 + i
                print(sum)
        else:
            print("Wrong input, choose between [1-10] or X to exit")

if __name__ == "__main__":
    main()

