# pa9b.py
# CS 453
# Written by Zainab Akinjobi
# Date written : 14th of April 2021
# Date /time last modified : 15th of April 2021 / 10pm
# Purpose : Using the os module to check if a file exists
# Input: External files
# Output : Differences between two strings


#Import module
import os

def main():
    #collect input files
    input_file1 = input('Enter the file name: ') #collecting name of input file from user
    input_file2 = input('Enter the file name: ') #collecting name of input file from user
    
    #Check if files exists
    if(os.path.exists(input_file1)): #checking if file1 exist

        if( os.path.exists(input_file2)): #checking if file2 exist
            
        #open the files 
            my_file_1 = open(input_file1,'r')  #open file1
            my_file1 =  my_file_1.readlines() #convert to list

            my_file_2 = open(input_file2 , 'r') #opening file for reading
            my_file2 =  my_file_2.readlines()      #read lines in my_files      
            for ii in range(len(my_file1)):  #range of the lines
                split1 = my_file1[ii] #split lines in file 1
                split2 = my_file2[ii] #split lines in file 2
    
    #Add '*' if characters are not the same and add space if they are the same
                if len(split1) <= len(split2): 
                    res = ""  			#initializing the difference
                    for jj in range(len(split1)):
                        if(split1[jj] == split2[jj]): #checking if characters are the same
                            res = res + " " #add space if characters are the same
                        else:
                            res = res + "*" #add star if characters are not the same
                    for jj in range(len(split2)-len(split1)):
                        res = res + "*"  #add star if character are not the same
                
    
                if len(split1) > len(split2): 
                    res = ""
                    for jj in range(len(split2)):
                        if(split1[jj] == split2[jj]):
                            res = res + " "  #add space if characters are the same
                        else:
                            res = res + "*"
                    for jj in range(len(split1)-len(split2)):
                        res = res + "*"
                            
    
                print("File 1: " + my_file1[ii]) #print the iith line from file1
                print("File 2: " + my_file2[ii]) #print the iith line from file2
                print("Diff: " + res)
         
                #Close the opened files
            my_file_1.close() #close file 1
            my_file_2.close() #close file 2
            
            #Implement the else statement
        else:
            print('Error: The second file does not exist.') #print the error statement

    else:
        print('Error: The first file does not exist.')#print the error statement

 


#calling the main function       
if __name__ == '__main__':
 # call the main function
   main( )       
        



                        
                        
                





    
    