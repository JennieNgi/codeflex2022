# Bug 1: in getInput(), if ( int(userInput) > 0 ): should be if ( userInput.isdigit() == True):
# Bug 2: in main(), calcOutput() should pass in the parameter

# Test Case 1 ----- 136
    # Enter change to return to customer: 136
    # $136 of the change to return to the customer
    # Number of $20s = 6
    # Number of $5s = 3
    # Number of $1s = 1
    # import math

# Test Case 2 ----- +
    # Enter change to return to customer: +
    # Error - incorrect input :(
    # $0 of the change to return to the customer
    # Number of $20s = 0
    # Number of $5s = 0
    # Number of $1s = 0

# Test Case 2 ----- -10
    # Enter change to return to customer: -10
    # Error - incorrect input :(
    # $0 of the change to return to the customer
    # Number of $20s = 0
    # Number of $5s = 0
    # Number of $1s = 0

# Test Case 2 ----- abc
    # Enter change to return to customer: abc
    # Error - incorrect input :(
    # $0 of the change to return to the customer
    # Number of $20s = 0
    # Number of $5s = 0
    # Number of $1s = 0

import math

def getInput():
    userInput = input("Enter change to return to customer: ")
    if ( userInput.isdigit() == True):
        return int(userInput) 
    else:
        print("Error - incorrect input :(")
        return 0

def calcOutput(change):

    print("$" + str(change), "of the change to return to the customer")

    twenties = math.floor(change / 20)
    change = change - (twenties * 20)
    fives = math.floor(change / 5)
    change = change - (fives * 5)
    ones = change

    print("Number of $20s =", twenties)
    print("Number of $5s =", fives)
    print("Number of $1s =", ones)

def main():
    change = getInput()

    calcOutput(change)

main()