import string
import random

def generate_password(length=12):
    # Define the pool of characters to choose from
    chars = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password from the character pool
    password = ''.join(random.choice(chars) for i in range(length))

    return password

# Generate a password with default length
password = generate_password()
print("Your password is:", password)

# Generate a password with custom length
custom_length = int(input("Enter the desired password length: "))
password = generate_password(custom_length)
print("Your password is:", password)
