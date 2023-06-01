"""
This code demonstrates all loop concepts and function in Python.

The code first defines a list of numbers.
Then, it uses a for loop to iterate through the list and print each number.
Next, it uses a while loop to keep looping until the user enters a negative number.
Finally, it uses a function to calculate the factorial of a number.
"""

# Define a list of numbers
numbers = [1, 2, 3, 4, 5]

# Iterate through the list and print each number
for number in numbers:
    print(number)

# Keep looping until the user enters a negative number
while True:
    number = int(input("Enter a number: "))
    if number < 0:
        break

# Define a function to calculate the factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Calculate the factorial of the user-input number
factorial_number = factorial(number)

# Print the factorial of the user-input number
print("The factorial of {} is {}".format(number, factorial_number))
