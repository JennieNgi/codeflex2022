###################     How the program should work    ########################

# Create a function that takes the input of the user (string) and returns the number (count) of vowels contained within it.
# Show the number of vowels in in the terminal.
# NOTE: The program should accept UPPERCASE or lowercase characters and ignore spaces.
#
# Example: 
# Enter string: CodeFLEX 
# Number of vowels are:
# 3

# --------------------------------------
# TEXT CASE: CodeFLEX
#
# Output-------------------
# Enter string: CodeFLEX 
# Number of vowels are:
# 3
# --------------------------------------
# TEXT CASE: 123456
#
# Output-------------------
# Enter string: 123456 
# Number of vowels are:
# 0
# --------------------------------------
# TEXT CASE: AEIOU aeiou
#
# Output-------------------
# Enter string:AEIOU aeiou
# Number of vowels are:
# 10


###########################################
######### Start coding here ###############
def main ():
    string=input("Enter string:")
    vowels=0
    for i in string:
        if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
            vowels=vowels+1
    print("Number of vowels are:")
    print(vowels)

main()

