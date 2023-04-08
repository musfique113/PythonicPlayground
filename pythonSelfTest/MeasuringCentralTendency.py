import statistics

# Function to get a list of numbers from the user
def get_numbers():
    numbers = []
    while True:
        num = input("Enter a number (or 'done' to finish): ")
        if num == 'done':
            break
        try:
            num = float(num)
            numbers.append(num)
        except ValueError:
            print("Invalid input. Please enter a number or 'done' to finish.")
    return numbers

# Get numbers from the user
numbers = get_numbers()

# Check if the list of numbers is empty
if not numbers:
    print("No numbers entered.")
else:
    # Calculate mean
    mean = statistics.mean(numbers)
    print("Mean: ", mean)

    # Calculate median
    median = statistics.median(numbers)
    print("Median: ", median)

    # Calculate mode
    try:
        mode = statistics.mode(numbers)
        print("Mode: ", mode)
    except statistics.StatisticsError as e:
        print("Mode: No mode found.")


