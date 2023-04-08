import statistics

# Function to get a list of numbers from the user
def get_numbers():
    numbers = []
    while True:
        try:
            num = float(input("Enter a number (or 'done' to finish): "))
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a number or 'done' to finish.")
        else:
            if num == 'done':
                break
    return numbers

# Get numbers from the user
numbers = get_numbers()

# Calculate mean
mean = statistics.mean(numbers)
print("Mean: ", mean)

# Calculate median
median = statistics.median(numbers)
print("Median: ", median)

# Calculate mode
mode = statistics.mode(numbers)
print("Mode: ", mode)
