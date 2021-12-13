# functions.py
# CS 453
# Written by Zainab Akinjobi
# Date written : 17th of March. 2021
# Date /time last modified : 18th of Feb. 2021 / 6pm
# Purpose : This program defines functions and assign arguments
# Input: Entered strings and integers
# Output :Arrange strings in fives ,types of triangles, neatly arranged odd numbers,





#printing 5 characters in an entered string in fives in newlines
def print5(x):                                                                 #The function print5 takes an argument 'x'
    for count in range(len(x)):                                                #Counts the length of "x" 
        if (count+1) % 5 == 0:                                                 #Count + 1 is divisible by 5 without remainder
            end = "\n"                                                         #Starts a new line
        else:
            end = ""                                                           #End without a new line
        print(x[count], end = end)      

print("Testing Function #1")                                                   #Test function 1
print()                                                                        #New line
num_to_print = input("Please enter a string: ")                                #Collects user input
print5(num_to_print)                                                           #Calls the function num_to_print
print()                                                                        #New line



        
#identififng types of triangles by entering 3 integers        
def triangleType(a,b,c):                                                       #Defines the function triangleType and passes arguement 'a,b,c'
    if a == b and b == c:                                                      # if a, b and c are equal
        return("equilateral")                                                  #It returns equilateral
    elif a == b and b != c:                                                    #If two of the arguements are equal
        return("isosceles")  
    elif b == c and a != c: 
        return("isosceles")
    elif a == c and b != c:
        return("isosceles")                                                    #It returns Isosceles
    else:
        return("scalene")                                                      #If the three are different it returns Scalene


print("Testing Function #2")                                                   #Testing function 2
print()                                                                        # print a new line
print("The triangle with side (1,1,1) is {}".format(triangleType(1,1,1)))      #calling the function triangleType and printing the corresponding return statement
print("The triangle with side (1,1,2) is {}".format(triangleType(1,1,2)))
print("The triangle with side (1,2,1) is {}".format(triangleType(1,2,1))) 
print("The triangle with side (2,1,1) is {}".format(triangleType(2,1,1)))
print("The triangle with side (2,8,1) is {}".format(triangleType(2,8,1)))
     
print()                                                                        #Print a new line


        
#printing Odd numbers and arranging them neatly in rows and columns      
def printOddNumbers(max):                                                      #Define the function printOddNumbers and it takes the arguement 'Max'
    print_width = len(str(max))+2                                              #length of the string +2
    space_count = 1                                                            #assign 1 to space count
    for count in range(1,max):                                                 #count in the range of 1 to max (excluding Max)
        if count % 2 != 0:                                                     #If count divided by 2 is not equal to zero
            if space_count % 10 == 0:                                          #If space count divided by 10 is 0
                end = "\n\n"                                                   #End in a new line
            else:
                end = ""                                                       #If not divivsible by 10, do not end in a new line
            if (count+1) == max:                                               #If count+ 1 equals max
                end = "\n"                                                     #end in a new line
            print("{:>{width}}".format(count, width = print_width), end = end) #format of the width
            space_count += 1  
        else:
            if (count+1) == max:                                               #If count+ 1 equals max
                print("")                                                      #New line

        
print("Testing Function #3")                                                   #Testing function 3
print()                                                                        #Newline

printOddNumbers(99)                                                            #Calling the arguement printOddNumbers with different arguements (3 times)
printOddNumbers(100)
printOddNumbers(1000)

           
