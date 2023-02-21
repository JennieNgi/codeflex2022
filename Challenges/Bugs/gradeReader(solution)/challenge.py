# Bug 1: the whole block of code inside the main() should be indented
# Bug 2: print("%-15s %-15s %-15s %-5s %-5s %-5s %-10s %s" % (gradeData[n][n], gradeData[n][n], gradeData[n][n], gradeData[n][n], gradeData[n][n], gradeData[n][n], gradeData[n][n], gradeData[n][n]) + "%") should be changed to print("%-15s %-15s %-15s %-15s %-15s %-15s" % (gradeData[n][0], gradeData[n][1], gradeData[n][2], gradeData[n][3], gradeData[n][4], gradeData[n][5]))
# Bug 3 : avgGrade = (int(gradeData[0][5]) + int(gradeData[1][5])  + int(gradeData[2][5])  + int(gradeData[3][5])  + int(gradeData[4][5])) / gradeData should be avgGrade = (int(gradeData[0][5]) + int(gradeData[1][5])  + int(gradeData[2][5])  + int(gradeData[3][5])  + int(gradeData[4][5])) / len(gradeData)

# Just run the program and terminal Output should be:
    # Subject         Challenges      Project I       Project II      Project III     FINAL GRADE     
    # Python          40              8               18              30              96
    # Java            30              10              20              25              85
    # Javascript      40              10              20              30              100
    # React           30              0               20              30              80
    # Database        40              10              20              20              90
    # The average grade is:  90.2

import csv

def main():

    infile = open("grades.csv", "r")
    csvReader = csv.reader(infile)
    gradeData = []
    for row in csvReader:
        gradeData.append(row)

    print("%-15s %-15s %-15s %-15s %-15s %-15s" % ("Subject", "Challenges", "Project I", "Project II", "Project III","FINAL GRADE"))

    for n in range(0, len(gradeData)):
        print("%-15s %-15s %-15s %-15s %-15s %-15s" % (gradeData[n][0], gradeData[n][1], gradeData[n][2], gradeData[n][3], gradeData[n][4], gradeData[n][5]))
        
    infile.close()

    avgGrade = (int(gradeData[0][5]) + int(gradeData[1][5])  + int(gradeData[2][5])  + int(gradeData[3][5])  + int(gradeData[4][5])) / len(gradeData)

    print("The average grade is: ", avgGrade)

main()