# Bug #1: in getProvinceAb(), for abbreviation in abbreviation: should be for abbreviation in abbreviations:
# Bug #2: in main(), abbreviations = data[1] fullNames = data[0] should be abbreviations = data[0] fullNames = data[1]
# Bug #3: in main(), result = getProvinceAb(userInput, abbreviations,fullNames) should be result = getProvinceAb(userInput.upper(), abbreviations,fullNames)

# TestCase 1 ----------------- MB
#     abbreviations >>>>>  ['NL', 'NS', 'NB', 'PE', 'QC', 'ON', 'MB', 'SK', 'AB', 'BC', 'YT', 'NT', 'NU']
#     fullNames >>>>>  ['NEWFOUNDLAND AND LABRADOR', ' NOVA SCOTIA', 'NEW BRUNSWICK', 'PRINCE EDWARD ISLAND', 'QUEBEC', 'ONTARIO', 'MANITOBA', 
#     'SASKATCHEWAN', 'ALBERTA', 'BRITISH COLUMBIA', 'YUKON', 'NORTHWEST TERRITORIES', 'NUNAVUT']
#     Enter either a full name or an abbreviation of a province/territory: MB
#     MANITOBA

# TestCase 2 ----------------- yukon (mindful this is lowercase)
#     abbreviations >>>>>  ['NL', 'NS', 'NB', 'PE', 'QC', 'ON', 'MB', 'SK', 'AB', 'BC', 'YT', 'NT', 'NU']
#     fullNames >>>>>  ['NEWFOUNDLAND AND LABRADOR', ' NOVA SCOTIA', 'NEW BRUNSWICK', 'PRINCE EDWARD ISLAND', 'QUEBEC', 'ONTARIO', 'MANITOBA', 
#     'SASKATCHEWAN', 'ALBERTA', 'BRITISH COLUMBIA', 'YUKON', 'NORTHWEST TERRITORIES', 'NUNAVUT']
#     Enter either a full name or an abbreviation of a province/territory: yukon
#     YT

import csv

def getInput():
    userInput = input("Enter either a full name or an abbreviation of a province/territory: ")
    return userInput

def getProvinceAb(userInput, abbreviations, fullNames):
    counter=0

    for abbreviation in abbreviations:
        if(abbreviation==userInput):
            return fullNames[counter]
        counter+=1

    counter=0
    for fullname in fullNames:
        if(fullname==userInput):
            return abbreviations[counter]
        counter+=1

    return -1


def main():

    infile = open("data.csv", "r")
    csvReader = csv.reader(infile)
    data = []
    for row in csvReader:
        data.append(row)
    print("abbreviations >>>>> ", data[0])
    print("fullNames >>>>> ", data[1])
    
    abbreviations = data[0]
    fullNames = data[1]

    userInput = getInput()

    result = getProvinceAb(userInput.upper(), abbreviations,fullNames)

    if(result != -1):
        print(result)
    else:
        print("The territory or province does not exist")    

main()