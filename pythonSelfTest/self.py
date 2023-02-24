import sys
def print_menu():
    print("1. Sum of 1 to n")
    print("2. Print 1 to n")
    print("3. Print factorila of n")
    print("4. Reverse string")
def main ():
    while True:
        print_menu()
        c = int(input("Enter choie [1-5]"))

        if c == 1:
            n = int(input("N: "))
            for i in range(n):
                print(i)
            else:
                print("exit")
                sys.exit()
if __name__ == "__main__":
    main()
