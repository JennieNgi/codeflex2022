# ***    HANGMAN    ***

# Guess a letter each turn to try and find the word
# - - - - - -
# Please guess a letter: s
# s - - - - - 
# Please guess a letter: c
# s c - - - - 
# Please guess a letter: h
# s c h - - - 
# Please guess a letter: o
# s c h o o - 
# Please guess a letter: o
# s c h o o - 
# Please guess a letter: l
# s c h o o l 
# ***    YOU WIN    ***

#Errors in order:
# getWinningWord should return winngingWord
# printGuess needs to receive guess list
# count is initialized within the for loop, it needs to be outside of the loop

# test cases:
# test a letter in the winning word, it should replace the - where it is in the word
# test a letter not in the winning word, it should not replace any of the -
# try entering multiple characters, it should tell you to enter a single letter
# make sure they can win the game
 
import random

def getWinningWord():
    words = ["python", "school", "coding", "student", "programming", "puzzle", "wavelength", "quiche", "lasagna"]
    winningWord = random.choice(words)
    return winningWord

def printGuess(guess):
    for item in guess:
        print(item, end = " ")

def userGuess(guess, word):
    count = 0
    while True:
        userInput = input("\nPlease guess a letter: ")
        if len(userInput) == 1:
            break
        else:
            print("\nPlease enter only a single character...")
            continue

    for character in word:
        if userInput == character:
            guess[count] = userInput
        count += 1

def main():
    word = getWinningWord()
    guess = []
    # for test purposes
    print(word)

    print("\n***    HANGMAN    ***\n\nGuess a letter each turn to try and find the word")
    for character in word:
        guess.append("-")
    while True:
        printGuess(guess)
        userGuess(guess, word)
        if "".join(guess) == word:
            printGuess(guess)
            print("\n***    YOU WIN    ***")
            break

main()