# #problem1
# n = int(input("Enter intiger: "))
# for i in range(n):
#     print(i+1)

# #problem2
# n = int(input("Enter number: "))
# sum = 0
# for i in range(n):
#     sum += i+1
# print(sum)
#Multiplication table
n = int(input("table"))
for i in range(1,11):
    print(n,"x",i,"=",n*i)
#Reverse a string: Write a program that takes a string as input and reverses it.
str = input("Give a string: ")
s = ""
for char in str:
    s = char + s
print(s)