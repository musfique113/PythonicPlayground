import random

# List of possible names
names = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace", "Hank", "Ivy", "Jack", "Kate", "Liam", "Mia", "Noah", "Olivia", "Paul", "Quinn", "Riley", "Sophia", "Tom"]

# Get user input for the range
#start = int(input("Enter the starting number: "))
start = 1
end = int(input("Enter the ending number: "))

# Generate random names for the specified range
for i in range(start, end + 1):
    random_name = random.choice(names)
    print(f"Name for {i}: {random_name}")
