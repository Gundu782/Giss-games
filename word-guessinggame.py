import random

# Step 2: Creating the Word Bank
word_bank = ["python", "coding", "program", "developer", "software", "debugging", "algorithm"]

# Step 3: Randomly select a word from the word bank
secret_word = random.choice(word_bank).lower()

# Step 4: Variables to Track Game State
max_attempts = 6
attempts = 0
guessed_letters = []
correct_guesses = ["_" for _ in secret_word]

print("Welcome to the Word Guessing Game!")
print("Guess the secret word, one letter at a time.")
print("You have 6 attempts to guess the word correctly.")
print("The word has", len(secret_word), "letters:", " ".join(correct_guesses))

# Step 5: Receiving and Validating Input
while attempts < max_attempts:
    guess = input("\nEnter a letter: ").lower()

    # Step 6: Validate the Guessed Word
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    # Step 7: Standardize the Word Bank and Guessed Word
    if guess in guessed_letters:
        print("You already guessed that letter. Try a different one.")
        continue

    guessed_letters.append(guess)

    # Step 8: Compare the Guessed Word
    if guess in secret_word:
        print(f"Good job! '{guess}' is in the word.")
        for i, letter in enumerate(secret_word):
            if letter == guess:
                correct_guesses[i] = guess
    else:
        print(f"Sorry, '{guess}' is not in the word.")
        attempts += 1

    # Step 9: Keeping the Game State Current
    print("Word so far:", " ".join(correct_guesses))
    print(f"Remaining attempts: {max_attempts - attempts}")

    # Step 10: Checking for a Win or Loss
    if "_" not in correct_guesses:
        print("\nCongratulations! You guessed the word:", secret_word)
        break
else:
    print("\nGame over! You've used all your attempts.")
    print("The secret word was:", secret_word)