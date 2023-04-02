# Define a function to apply Caesar cipher
def caesar_cipher(text, shift):
    cipher_text = ""
    for char in text:
        if char.isalpha():
            # Convert to uppercase for easier calculation
            char = char.upper()
            # Apply shift and wrap around if necessary
            cipher_char = chr((ord(char) - 65 + shift) % 26 + 65)
            # Append to cipher text
            cipher_text += cipher_char
        else:
            # Append non-alphabetic characters as is
            cipher_text += char
    return cipher_text

# Ask for user input and shift value
text = input("Enter plain text to be encrypted: ")
shift = int(input("Enter shift value: "))

# Apply Caesar cipher and output cipher text
cipher_text = caesar_cipher(text, shift)
print("Cipher text: ", cipher_text)
