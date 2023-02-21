# A palindrome is a word that says the same thing when you spell it backwards
# The words "racecar" and "tacocat" are examples of this.
# This challenge is to create a program that takes a string input
# When the input is entered, your code will need to check if the imput word is a palindrome
# If the input is a palindrome, the output should look like this:
    # >>> Wow! [input] is a palindrome!
# If it is not a palindrome, output should be:
    # >>> Lame! [input] isn't a palindrome.

# your code goes below here!
# ----------------------------------------------------------------
myWord = input("Enter a word to check if it's a palindrome: ")

def isPalendrome(stringy):
    if (bool(stringy == stringy [::-1])):
        print(">>> Wow! \'" + stringy + "\' is a palindrome!")
    else:
        print(">>> Boring. \'" + stringy + "\' isn't palindrome.")

isPalendrome(myWord)


