#Errors in order:
# in compare() the returns need to return either you win or you lose 
# in main() need to call rockPaperScissors() and not playRPS()

# test cases:
# one where they win, one where they lose, and one where it ties

import random

def rockPaperScissors():
    compChoice = inputToString(random.randint(1, 3))
    print("\nFor testing purposes, the computer has chosen " + compChoice)
    userChoice = inputToString(userInput()) 
    print("\nYou have chosen " + userChoice)
    print("The computer has chosen " + compChoice + "\n")
    return compare(userChoice, compChoice)

def compare(userChoice, compChoice):
    if userChoice == compChoice:
        return "It's a tie!"
    elif userChoice == "ROCK" and compChoice == "SCISSORS":
        return "YOU WIN!"
    elif userChoice == "PAPER" and compChoice == "ROCK":
        return "YOU WIN!"
    elif userChoice == "SCISSORS" and compChoice == "PAPER":
        return "YOU WIN!"
    else:
        return "YOU LOSE!"
    
def inputToString(num):
    if num == 1: 
        return 'ROCK' 
    elif num == 2: 
        return 'PAPER' 
    else:
        return 'SCISSORS' 
    
def userInput():
    choice = -1
    while choice not in range(1, 4):
        try:
            choice = int(input("Please enter a number from 1 to 3: "))
        except KeyboardInterrupt:
            exit()
        except:
            print("that's not a valid number")
    return choice
    
def main():
   print("*** ROCK PAPER SCISSORS ***\n\nType the number corresponding to the option you want to choose:")
   while True:
        print("\n1. Rock\n2. Paper\n3. Scissors\n")
        print(rockPaperScissors())
        again = input("\nWould you like to play again? Type y or yes to play again: ")
        if again.lower() == "y" or again.lower() == "yes":
            continue
        else:
            print("\nThanks for playing!")
            break

main()