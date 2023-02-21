#*****************How the program should work*******************.
# The program should print the words of a modified version of the famous bottles of beer game, 
# it starts at 1 and it ends on 99

# Example of the first 3 lines of the output and the last line of the output:
#1 bottle of beer on the wall. 1 bottle of beer. Take one down, pass it around, 0 bottles of beer on the wall.
#2 bottles of beer on the wall. 2 bottles of beer. Take one down, pass it around, 1 bottle of beer on the wall.
#3 bottles of beer on the wall. 3 bottles of beer. Take one down, pass it around, 2 bottles of beer on the wall
#...
#98 bottles of beer on the wall. 98 bottles of beer. Give one back, 99 bottles of beer on the wall.

# Notice the first 2 lines use the word bottle instead of bottles where necessary

#****************Your challenge*********************************
# Fix all the bugs so that the program runs and does what its supposed to do correctly.

#********** TEST CASES
#These are the first 3 lines of the output:
#1 bottle of beer on the wall. 1 bottle of beer. Give one back, 2 bottles of beer on the wall.
#2 bottles of beer on the wall. 2 bottles of beer. Give one back, 3 bottles of beer on the wall.
#3 bottles of beer on the wall. 3 bottles of beer. Give one back, 4 bottles of beer on the wall.


#These are the 3 last lines of the output
#96 bottles of beer on the wall. 96 bottles of beer. Give one back, 97 bottles of beer on the wall.
#97 bottles of beer on the wall. 97 bottles of beer. Give one back, 98 bottles of beer on the wall.
#98 bottles of beer on the wall. 98 bottles of beer. Give one back, 99 bottles of beer on the wall.



def main():
       
    #print cases second to last and last
    print("1 bottle of beer on the wall. 1 bottle of beer. Give one back, 2 bottles of beer on the wall.")
    #print all the cases that are similar 
    for n in range(2,99):
        print(str(n) + " bottles of beer on the wall. " + str(n) + " bottles of beer. Give one back, " + str(n+1) + " bottles of beer on the wall.")

main()