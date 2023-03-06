# Write a Python program to simulate a game of Hangman. The program should do the following:

# Select a random word from a list of words
# Prompt the user to guess a letter
# If the letter is in the word, reveal the positions of the letter in the word and prompt the user to guess another letter
# If the letter is not in the word, subtract one from the user's remaining guesses and prompt the user to guess another letter
# If the user correctly guesses all the letters in the word, print a victory message
# If the user runs out of guesses without correctly guessing all the letters, print a defeat message
# You can choose any list of words to use in your program. Be sure to give the user feedback on which letters they have already guessed, and keep track of the user's remaining guesses. You may also want to include an option for the user to quit the game at any time.

import random

# Define a list of words
words = ['python', 'java', 'ruby', 'javascript', 'php', 'html', 'css', 'swift']

# Select a random word from the list
word = random.choice(words)

# Create an empty list to store the user's guesses
guesses = []

# Set the maximum number of incorrect guesses
max_guesses = 6

# Loop until the user either guesses the word or runs out of guesses
while True:
    # Print the current state of the word
    for letter in word:
        if letter in guesses:
            print(letter, end=' ')
        else:
            print('_', end=' ')
    print()
    
    # Get a guess from the user
    guess = input('Guess a letter: ')
    
    # Check if the guess is already in the list of guesses
    if guess in guesses:
        print('You already guessed that letter.')
    # Check if the guess is in the word
    elif guess in word:
        print('Good guess!')
        # Add the guess to the list of guesses
        guesses.append(guess)
        # Check if the user has guessed all the letters in the word
        if all(letter in guesses for letter in word):
            print('Congratulations, you guessed the word!')
            break
    # If the guess is not in the word
    else:
        print('Sorry, that letter is not in the word.')
        # Subtract one from the user's remaining guesses
        max_guesses -= 1
        # Check if the user has run out of guesses
        if max_guesses == 0:
            print('Sorry, you ran out of guesses. The word was', word)
            break
    
    # Print the number of remaining guesses
    print('You have', max_guesses, 'guesses left.')
    # Print the list of letters the user has already guessed
    print('Letters you have already guessed:', guesses)
