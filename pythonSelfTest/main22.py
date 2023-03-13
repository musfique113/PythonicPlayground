import random

# Create a list of random integers
my_list = [random.randint(0, 100) for _ in range(10)]

# Print the list
print(my_list)

# Find the largest and smallest numbers in the list
largest = max(my_list)
smallest = min(my_list)

# Print the largest and smallest numbers
print("The largest number is:", largest)
print("The smallest number is:", smallest)
