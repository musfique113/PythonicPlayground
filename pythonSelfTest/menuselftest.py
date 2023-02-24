import sys
def menu_print():
    print("1. Print 1 to n")
    print("2. Print sum of 1 to n")
    print("3. Print table")
    print("4. Print reverse string")
    print("5. Print factorial of n")
def main():
    while True:
        menu_print
        choise = int(input("Choise [1-5]: "))
        if choise == 1:
            n = int(input("N: "))
            for i in range(n):
                print(i)
        elif choise == 2:
            n = int(input("N: "))
            sum = 0
            for i in range(n):
                sum += i +1
                print(sum)
        elif choise == 3:
            n = int(input("N: "))
            for i in range(1, 11):
                print(i, "X", n, "=", i*n)
        elif choise == 4:
            s = input("String: ")
            str = ""
            for char in s:
                str = char + str
                print(str) 
        elif choise == 5:
            n = int(input("N: "))
            fact = 1
            for i in range(1, n+1):
                fact *= i
                print(fact)
        else:
            print("wrong")
        sys.exit()
        
if __name__ =="__main__":
    main()
