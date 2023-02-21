# The current year is 2022. Global population is approximately 7,850,000,000
# Your task is to calculate estimated global population growth between now and year 2050.
# Each year the population is estimated to grow by 1%

# Starting from 2022, your code should output the population for every year until 2050
# EX OUTPUT: 
# >>> In 2023, the world population will be 7928500000.0
# >>> In 2024, the world population will be 8007785000.0
# >>> In 2025, the world population will be 8087862850.0
# ...
# >>> In 2050, the world population will be 10372134090.151274

# Good luck!

# your code goes below here!
# ----------------------------------------------------------------
year = 2022
population = 7850000000
ogPopulation = population

while year<2050:
    year = year + 1
    population = population * 1.01
    print("In " + str(year) + ", the world population will be " + str(population))