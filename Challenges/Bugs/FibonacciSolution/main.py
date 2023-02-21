# Bugs in order
# need to convert user input for numTerms from string to int
# count only needs to iterate by 1 every loop instead of being set to sum

# test case: use 15 terms, it should look like this:
# How many terms of the Fibonacci sequence would you like to see? 15
# Fibonacci sequence up to 15 terms:
# 0
# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 144
# 233
# 377

def main():
    numTerms = -1
    while numTerms <= 0:
        try:
            numTerms = int(input("How many terms of the Fibonacci sequence would you like to see? "))
            if numTerms <= 0:
                print("Please enter a positive integer")
        except KeyboardInterrupt:
            exit()
        except:
            print("thats not a number...")

    num1, num2 = 0, 1
    count = 0

    print("Fibonacci sequence up to " + str(numTerms) + " terms:")

    while count < numTerms:
        print(num1)
        sum = num1 + num2
        num1 = num2
        num2 = sum
        count += 1

main()