import sys
def menu():
    print("1. Print 1 to N")
    print("2. Print sum of N")
    print("3. Print table")
    print("4. Print reverse array")
    print("5. Print factorial of N")
    print("6. exit")
def main():
    menu()
    while True:
        choise = int(input("Enter choise: "))
        if choise == 1:
            N = int(input("N: "))
            for i in range(N+1):
                print(i)
        elif choise == 6:
            print("Programme closed")
            sys.exit()
        elif choise == 2:
            N = int(input("N: "))
            sum = 0
            for i in range(N):
                sum += 1 + i
                print(sum)
        elif choise == 3:
            N = int(input("N: "))
            for i in range(1,11):
                print(N ,"X", i,"=",i*N)
        elif choise == 4:
            stry = input("Input array: ")
            s = ""
            for char in stry:
                s = char + s
                print(s)
        elif choise == 5:
            n = int(input("N: "))
            fac = 1
            for i in range(1, n+1):
                fac *= i 
                print(fac) 
        else :
            print("Wrong Input, choose between [1-6]")
            
if __name__ == "__main__":
    main()