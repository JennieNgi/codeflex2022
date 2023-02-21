#*****************How the program should work*******************.
# The program prints a 5 digit lottery number.  Each one of these digits is a random number between 1 and 9.
# The 5 numbers should be printed next to each other
# Example of result:
# 17762
# If you notice, it is fine to have reapeated digits.

#****************Your challenge*********************************
# Fix all the bugs so that the program runs and does what it's supposed to do correctly.

#****************TEST CASES
#Run the program 3 times
#In each run check that the output has a 5 digit number(not shorter, not longer).  Count the digits!! 
#The output should not have any zeros


import random

def generateLotteryNumbers():
    firstNumber = random.randint(1,9)
    secondNumber = random.randint(1,9)
    thirdNumber = random.randint(1,8)
    fourthNumber = random.randint(1,9)
    fifthNumber = random.randint(1,9)
    
    print (("%1s%1s%1s%1s%1s")%(firstNumber,secondNumber,thirdNumber,fourthNumber,fifthNumber))

def main():
    generateLotteryNumbers()
main()
