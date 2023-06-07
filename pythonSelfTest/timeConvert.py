import time

def convert_seconds(seconds):
  hours = seconds // 3600
  minutes = (seconds % 3600) // 60
  seconds = seconds % 60

  return hours, minutes, seconds

def main():
  seconds = int(input("Enter the number of seconds: "))

  hours, minutes, seconds = convert_seconds(seconds)

  print("The time in hours, minutes, and seconds is:", hours, ":", minutes, ":", seconds)

if __name__ == "__main__":
  main()
