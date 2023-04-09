import statistics
from tabulate import tabulate

# Function to get a list of grouped data from the user
def get_grouped_data():
    grouped_data = []
    while True:
        group = input("Enter a group (or 'done' to finish): ")
        if group == 'done':
            break
        try:
            values, frequency = group.split(':')
            lowest_value, highest_value = map(int, values.split('-'))
            frequency = int(frequency)
            for value in range(lowest_value, highest_value + 1):
                grouped_data.extend([value] * frequency)
        except (ValueError, TypeError):
            print("Invalid input. Please enter a valid group in the format 'lowest_value-highest_value:frequency' or 'done' to finish.")
    return grouped_data

# Get grouped data from the user
grouped_data = get_grouped_data()

# Check if the list of grouped data is empty
if not grouped_data:
    print("No grouped data entered.")
else:
    # Display input values and frequency in tabular format
    data = []
    for value in sorted(set(grouped_data)):
        frequency = grouped_data.count(value)
        data.append([value, frequency])
    headers = ["Value", "Frequency"]
    print("Input Values and Frequency:")
    print(tabulate(data, headers=headers, tablefmt="grid"))
    print()

    # Calculate mean
    mean = statistics.mean(grouped_data)

    # Calculate median
    median = statistics.median(grouped_data)

    # Calculate mode
    try:
        mode = statistics.mode(grouped_data)
    except statistics.StatisticsError as e:
        mode = "No mode found."

    # Calculate standard deviation
    stdev = statistics.stdev(grouped_data)

    # Calculate variance
    variance = statistics.variance(grouped_data)

    # Display statistics in tabular format
    data = [["Mean", mean],
            ["Median", median],
            ["Mode", mode],
            ["Standard Deviation", stdev],
            ["Variance", variance]]
    headers = ["Statistic", "Value"]
    print("Calculated Statistics:")
    print(tabulate(data, headers=headers, tablefmt="grid"))
