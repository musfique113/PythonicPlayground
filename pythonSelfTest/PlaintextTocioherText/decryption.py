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

# Define a function to decode Caesar cipher
def caesar_decode(cipher_text, shift):
    # Apply Caesar cipher with opposite shift
    plain_text = caesar_cipher(cipher_text, -shift)
    return plain_text

# Ask for user input and shift value
cipher_text = input("Enter cipher text to be decrypted: ")
shift = int(input("Enter shift value: "))

# Decode Caesar cipher and output plain text
plain_text = caesar_decode(cipher_text, shift)
print("Plain text: ", plain_text)
