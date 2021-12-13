# stringFunctions.py
# CS 453
# Written by Zainab Akinjobi
# Date written : 29th of Mar. 2021
# Date /time last modified : 30th of Mar. 2021 / 6pm
# Purpose : This program tests different string functions
# Input: String Functions
# Output : Print new strings

#using a remove_punc function
def remove_punc(s):        #define the function remove_punc and passing an arguement s.
    result = ""            #assign empty space to result
    spaces = ["\t"," ", "\n"]  #define the function space
    for ii in s:           #using for loop
        
        if ii.isalnum() == True or ii.isspace() == True or ii in spaces: # using an if statement
            result = result + str(ii)  #concatenating result and the string
    return(result)                 #return the new elements in result

# Using the word_count function
def word_count(s): #define the function word_count and pass the arguement s
    word_list = s.split(" ") #split the words in word_list when there are spaces
    return(len(word_list))   #return the number of words_list

def add_unique(s, word_list): #define the function add_unique and pass the arguement s, word_list
    s_split = s.split(" ") #split the words in s_split
    for word in s_split:  #Using a for loop
        if word not in word_list: #Using an if statement 
            word_list.append(word.lower()) #append wordlist to word and covert the words to lowercase

def main(): #writing statements to test functions
    
    # Testing remove_punc
    print("Testing remove_punc function first time")
    print()
    myString_1 = input('Type something with punctuation: ') # Taking input
    newString_1 = remove_punc( myString_1 ) # passing input to remove_punc function; call remove_punc
    print()
    print('Here is the string without punctuation: ', newString_1) # Displaying the input string without any punctuation
    print()
    
    print("Testing remove_punc function second time")
    print()
    myString_2 = input('Type something with punctuation: ') # Taking input
    newString_2 = remove_punc( myString_2) # passing input to remove_punc function; call remove_punc
    print()
    print('Here is the string without punctuation: ', newString_2) # Displaying the input string without any punctuation
    print()
    
    # Testing word_count
    print("Testing word_count function first time")
    print()
    print("The number of words in the first entered string without punctuation is: ", word_count(newString_1)) # Counting the number of words in user input after removing punctuation
    print()
    
    print("Testing word_count function second time")
    print()
    print("The number of words in the second entered string without punctuation is: ", word_count(newString_2)) # Counting the number of words in user input after removing punctuation
    print()
    
    # Testing add_unique
    print("Testing add_unique function first time")
    print()
    word_list_1 = "This is where you will write statements to test the 3 functions above".split(" ") # making up an intial word list
    print("Initial word list is: ", word_list_1) # Displaying the intial word list
    print()
    add_unique(newString_1, word_list_1) # passing the user input without puntuation to add_unique for addition to the word list recently created
    print("New word_list is: ", word_list_1) # displaying the new word list
    
    print("Testing add_unique function second time")
    print()
    word_list_2 = ["Testing", "add_unique"] # making up an intial word list
    print(" Second initial word list is: ", word_list_2) # Displaying the intial word list
    print()
    add_unique(newString_2, word_list_2) # passing the user input without puntuation to add_unique for addition to the word list recently created
    print(" Second new word_list is: ", word_list_2) # displaying the new word list
    
    
if __name__ == '__main__':
 # call the main function
    main( )

