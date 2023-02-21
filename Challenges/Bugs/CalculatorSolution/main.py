# Errors in order
# multiply is written as x instead of * in multiply()
# in divide() it checks if num1 is zero instead of num2
# in main() if the user inputs something invalid for num1 the program crashes, the if statements should be in the try block

# Test cases:
# 5 + 5 should equal 10
# 5 * 5 should be 25
# 5 / 0 should say you cannot divide by zero
# if you choose a letter instead of a number for the first number, it should not crash and should say "that's not a number" and the program will end

def add(num1, num2):    
    print (num1, " + ", num2, " = ", num1 + num2)

def subtract(num1, num2):    
    print (num1, " - ", num2, " = ", num1 - num2) 

def multiply(num1, num2):   
    print (num1, " * ", num2, " = ", num1 * num2)  

def divide(num1, num2): 
    if num2 == 0:
        print("Cannot divide by zero")
    else:    
        print (num1, " / ", num2, " = ", num1 / num2) 

def main():  
    print ("Please select the operation.")    
    print ("a. Add")    
    print ("b. Subtract")    
    print ("c. Multiply")    
    print ("d. Divide")    
        
    choice = input("Please enter choice (a/ b/ c/ d): ")    

    if choice == 'a' or choice == 'b' or choice == 'c' or choice == 'd':
        try:
            num1 = int (input ("Please enter the first number: "))    
            num2 = int (input ("Please enter the second number: "))
            if choice == 'a':    
                add(num1, num2)  
                
            elif choice == 'b':    
                subtract(num1, num2)   
                
            elif choice == 'c':    
                multiply(num1, num2)  

            elif choice == 'd':    
                divide(num1, num2)  
        except KeyboardInterrupt:
            exit()
        except:
            print("that's not a number...")
        
    else:    
        print ("This is an invalid input")   

main() 