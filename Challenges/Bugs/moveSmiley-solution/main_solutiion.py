#*****************How the program should work*******************.
# In this program the user can enter a number between 1 and 40, and the smiley face :) is 
# printed twice as many spaces to the right as the entered number. 
# If the user enters an invalid input, the program should print the following message: x( [Your input killed :)]

#****************Your challenge*********************************
# Fix all the bugs so that the program runs and does what its supposed to do correctly.

#****************Test cases********************************
#How many characters would you like to move :)? 1
#  :)

#How many characters would you like to move :)? 4
#        :)

#How many characters would you like to move :)? -1
#x( [Your input killed :)]

#How many characters would you like to move :)? 41
#x( [Your input killed :)]


from tokenize import String


def getUserInput():
    return int(input("How many characters would you like to move :)? "))
   
def main():
    #print first smiley
    print(":)")
    
    #validate whole numbers
    try:
        # put in spaces the user input
        spaces = getUserInput()
    except ValueError:
        print("x( [Your input killed :)]")
        #exit main/program
        return

    if(spaces>=1 and spaces<=40):
        #calculate how many spaces the string will occupy
        occupiedSpace=((spaces)*2)+2
        formatSpecifier="%"+str(occupiedSpace)+"s"
        #print output with spaces
        print(formatSpecifier%":)")
    else:
        #when not in range
        print("x( [Your input killed :)]")

main();