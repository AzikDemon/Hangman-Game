from random import randint

lives = 5 # Feel free to change to make it easier or harder
lengthOfMinimumWord = 5 # Feel free to change to make the word length requirement higher / lower

with open('words.txt', 'r') as f:
  fileContent = f.read()
words = fileContent.split()

while True:
  wordChoiceNum = randint(0, len(words) - 1)
  if len(words[wordChoiceNum]) > lengthOfMinimumWord:
    wordChoice = words[wordChoiceNum] 
    break

for i in range(len(wordChoice)):
  print("_", end = " ")
print(f"Word Length: {len(wordChoice)}")

guessedWord = ["_"] * len(wordChoice)
previousGuesses = []

while True:

  guess = input("Guess a letter: ")
  if not (isinstance(guess, str) and guess.isalpha() and len(guess) == 1):
    print("Must be a letter")
  else:
    if guess in previousGuesses:
      print(f"You have already guessed {guess}")
    else:
      previousGuesses += guess
      correctGuess = False 

      for index in range(len(wordChoice)):
        if guess == wordChoice[index]:
          guessedWord[index] = guess
          correctGuess = True
      print(" ".join(guessedWord)) 

      if "_" not in guessedWord:
        print(f"Congratulations! You guessed the word. The word was {wordChoice}")
        break

      if not correctGuess:
        lives -= 1
        if lives == 0:
          print(f"Game over, you ran out of lives. The word was {wordChoice}")
          break
        print(f"The letter '{guess}' is not in the word. Lives left: {lives}")