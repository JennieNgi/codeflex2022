# In the game Dungeons and Dragons, they use a set of 6 different dice to play.
# Write a program in which you choose a specific sided die to roll (4,6,8,10,12,20) 
# and output a correct random die roll for that particular sided die 
#(eg. for d20 die output a random number between 1 and 20)
#
# *layout*
#
# Dungeons & Dragons Dice Roller
# Choose a number of sided dice to roll - 4 , 6, 8 , 10 , 12 or 20
# > d: X
# You rolled the DX die, and rolled a Y

####
#### solution test criteria
## its hard to test random numbers.
## test the 4 sided die...should be between 1 & and 5
## do some tests on the 20 to see if you get a decent range of numbers 
# 
# ####

import random

print ("Dungeons & Dragons Dice Roller")
print("Choose a number of sided dice to roll - 4 , 6, 8 , 10 , 12 or 20")


number = input("d: ")

roll = int(random.randint(1, int(number)))

print("You rolled the D" + str(number) + " die, and rolled a " + str(roll))
    
