import sys
def choise():
    print("Chooise between [1-10] or Xo close the program")

def main():
    choise()
    while True:
        opt = input("Your choise: ")
        if opt == "1":
            n = int(input("Print 1 to n, n = : "))
            for i in range (n+1):
                print(i)
        elif opt == "X" and opt == "x":
            print("Exited")
            sys.exit()
        else:
            print("Wrong input, choose between [1-10] or X to exit")

if __name__ == "__main__":
    main()

