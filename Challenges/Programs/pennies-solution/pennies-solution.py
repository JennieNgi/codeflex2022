# Would you rather have $1,000,000 now...or be given a single penny that doubles everyday for a month?
# Every time you double the penny, the number of pennies you have increases exponentially (1, 2, 4, 8, 16, 32 ,64 etc)

# CHALLENGE:
# Create a function that calculates the $$$ amount of your penny after doubling that penny every day for a month (30 days).
# Is it more or less than $1,000,000?

# Rememeber there are 100 pennies in $1.
# Rememer that you are given your first penny on the first day of the month and then it starts doubling on the second day

# Output
# Doubling your penny every day for 30 days = $???????.??

## Solution Answer
## Doubling your penny every day for 30 days = $5368709.12

daycounter = 1
numofpennies = 1
# the number of days to use for the calculation is 29 since on day 1 you get the penny and it doesnt double on that day
days= 29

while daycounter <= days:   
    numofpennies *= 2  
    # convert to $$$ amount
    dollartotal = numofpennies/100
    daycounter += 1

print ("Doubling your penny every day for 30 days = " + "$"+str(dollartotal) )     




    
