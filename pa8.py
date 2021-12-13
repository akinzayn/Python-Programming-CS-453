# pa8.py
# CS 453
# Written by Zainab Akinjobi
# Date written : 8th of April. 2021
# Date /time last modified : 8th of April. 2021 / 6pm
# Purpose : Read in data from a file 
# Input: getting input from an External file
# Output : Modified external file content 

#testing def function
def  remove_non_alpha(s):
    result = ""            #assign empty space to result
    for ii in s:           #using a for loop
        if ii.isalnum() == True and ii.isdigit() == False: # using an if statement to return just alphabet
            result = result + str(ii)  #concatenating result and the string
    return(result)               
    
 #collecting external input   
def main():
    input_file_name = input('Enter the file name: ') #collecting name of input file from user
    
    output_file_name = input('Enter the output file name: ')  #collecting name of output file from user
    
    inputFile = open(input_file_name,"r") #open the input file for reading
    outputFile = open(output_file_name, 'w+') #open the output file for writing

    
    for line in inputFile:
        slice_ind = slice(-1) #remove the newline character using slice
        line = line[slice_ind]
#perform modifications
        list_of_words = line.split() #split the string into a list
        print(list_of_words)
        list3A = [ x.lower() for x in list_of_words ] #covert the word to lower case
        list3B = [remove_non_alpha(x) for x in list3A if x != ""] #remove all none character from the list
        print(list3B) #print list 3B
        list3C = [len(x) for x in list3B] #assign the length of 3B with 3c
        average = sum(list3C)/len(list3C)# find the average of list 3C
        outputFile.write("Original line:" + line + '\n') #original line from input file
        outputFile.write("Words:" + " ".join(list3A) + '\n')# elements of list3A with one space between elements
        outputFile.write("Only Letters:" + " ".join(list3B) + '\n')# elements of list3B with one space between elements
        outputFile.write("Average word length:" + str(average) + '\n') #average length of each lines
        outputFile.write('\n') #blank line
        
    #close both files
    outputFile.close() #close output file
    inputFile.close() #close input file
        
        
 #calling the main function       
if __name__ == '__main__':
 # call the main function
   main( )       
        
        
        

    
   