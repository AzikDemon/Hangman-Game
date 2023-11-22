from random import choice

lives = 5  # Number of lives
lengthOfMinimumWord = 5  # Minimum word length

# Read words from file and filter based on minimum word length
with open('words.txt', 'r') as f:
    words = [word.strip() for word in f if len(word.strip()) > lengthOfMinimumWord]

wordChoice = choice(words)  # Choose a random word from the list
guessedWord = ["_"] * len(wordChoice)  # Initialize guessed word with underscores
previousGuesses = set()  # Set to store previous guesses

print(" ".join(guessedWord))
print(f"Word Length: {len(wordChoice)}")

while True:
    guess = input("Guess a letter: ")

    if len(guess) != 1 or not guess.isalpha():
        print("Must be a letter")
    else:
        if guess in previousGuesses:
            print(f"You have already guessed {guess}")
        else:
            previousGuesses.add(guess)
            correctGuess = False

            # Check if the guess is correct
            for index, letter in enumerate(wordChoice):
                if guess == letter:
                    guessedWord[index] = guess
                    correctGuess = True

            print(" ".join(guessedWord))

            # Check if the word has been completely guessed
            if "_" not in guessedWord:
                print(f"Congratulations! You guessed the word. The word was {wordChoice}")
                break

            # Check if the guess is incorrect
            if not correctGuess:
                lives -= 1

                if lives == 0:
                    print(f"Game over, you ran out of lives. The word was {wordChoice}")
                    break

                print(f"The letter '{guess}' is not in the word. Lives left: {lives}")
