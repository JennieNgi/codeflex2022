# What Day were you born?
# Write a program to input your date of birth in DD MM YYYY format and it will output the day of the week you were born on
# INPUT
# Enter the date(for example:12 31 2022): XX XX XXXX
# Output
# You were born on a XXXDAY

##TESTING
## Input 22 08 1971
## You were born on a Sunday
## Input 12 31 1999
## You were born on a Friday

import datetime

date=str(input('Enter the date(for example:12 31 2022):'))
day = datetime.datetime.strptime(date, '%m %d %Y').weekday()
day_name= ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
print(('You were born on a ') + str(day_name[day])) 

    
