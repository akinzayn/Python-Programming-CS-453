# pa9a.py
# CS 453
# Written by Zainab Akinjobi
# Date written : 14th of April. 2021
# Date /time last modified : 14th of April 2021 / 6pm
# Purpose : Using the os module to check if a file exists
# Input: External files
# Output : Replacing old strings in a file with new strings

 #collecting external input   
import os   #import the os module
def main():  #main function
    
    input_file1 = input('Enter the file name: ') #collecting name of input file from user
    input_file2 = input('Enter the file name: ') #collecting name of input file from user
    
    #Checkng if file exists
    if(os.path.exists(input_file1)): 
        my_file1 = open(input_file1,'r') #opening file one for reading
        print("Exist")                   #prints exists if file 1 exists
        my_file2 = open(input_file2 , 'w+')  #open file 2 for writing
    
        old_string = input('Enter a string : ')  #Collect input from user and store it in a variable
        
        new_string = input('Enter a new string : ')  #Collect input from user and store it in a variable
        
        #Replace occurences of old string with new string
        for line in my_file1: 
            line = line.replace(old_string, new_string) #replace old string with a new one
            my_file2.write(line) # write the files to line two
        
        #close the file
        my_file1.close() #closing file 1
        my_file2.close() #closing file 2
    #implement the else statement if the file does not exist    
    else:           
        print('Error: The file does not exist.') #Print the error message

 

#calling the main function       
if __name__ == '__main__':
 # call the main function
   main( )       
        






    
    