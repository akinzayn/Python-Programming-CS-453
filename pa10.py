

# pa10.py
# CS 453
# Written by Zainab Akinjobi
# Date written : 29th of April. 2021
# Date /time last modified : 29th of April. 2021 / 6pm
# Purpose : This program tests different string functions
# Input: Module 10
# Output : Tally alphabet with frequency
    
import module10

def main():                                                                          #write a main function
    print( module10.remove_non_alpha( "123xyz#$%" ))    
    user_input = input("Enter the file name: ")                       #collect file name  
    """Echo the contents of a file."""
    f = open(user_input)                                                     #open file
    total_count = 0                                                            #set total count to zero
    unique_word_list = []
    file_letter_freq = [0 for  i in range(26)]                         #Iterate over the file using a for loop
    alphabets = [chr(i) for i in range(ord('a'), ord('z')+1)]

    for line in f:
        slice_ind = slice(-1)
        line = line[slice_ind]
        no_punct_line = module10.remove_punc(line)
        total_count = total_count + module10.word_count(no_punct_line) #count total number of  words in file
        module10.add_unique(no_punct_line, unique_word_list)
        file_letter_freq = [file_letter_freq[i] + module10.letter_frequency(no_punct_line)[i] for i in range(26)]                          #tally frequencies of letters in file
    
    f.close()                           #close file
    unique_word_list.sort()        #sort list of unique words
    
    print()                                   #newline
    print("The file contains ", total_count, " words") #print the total number of words in the file
    print()
    print("There were ",  len(unique_word_list)," unique words")  #print the unique words one word per line
    print()                                   #newline
    for i in range(len(unique_word_list)):
        print("{:>{width1}}. {}".format(i+1, unique_word_list[i], width1 = len(str(len(unique_word_list)+1)) ))  
    
    print()    
    print("{} {}".format("Letter", "Frequency"))     #print frequency in neatly aligned 2-column format
    print("{:>{width1}} {:>{width2}}".format("------", "---------", width1 = 6, width2 = 9))
    for i in range(26):
        print("{:^{width1}} {:^{width2}}".format(alphabets[i],file_letter_freq[i] , width1 = 6, width2 = 9))
        
    
    
    
if __name__ == '__main__':
 # call the main function
    main( )
