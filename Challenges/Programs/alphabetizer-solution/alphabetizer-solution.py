# Alphabetizer
# Write a program to take the string of words below and put them into alphabetical order removing the commas
#
# input data for challenge:  idiots,hate,girls,funny,everything,do,can,boys,annoying
#
# Output
#
# ***Alphabetizer***
# UnSorted words:
# idiots,hate,girls,funny,everything,do,cant,boys,annoying
# Sorted words:
# annoying boys can do everything funny girls hate idiots

print ("***Alphabetizer***")

print ("UnSorted Words:")
raw = "idiots,hate,girls,funny,everything,do,cant,boys,annoying"
print (raw)
print ("Sorted Words:")

#SOLUTION
words = raw.split(",")
words.sort()
print (' '.join(words))

    
