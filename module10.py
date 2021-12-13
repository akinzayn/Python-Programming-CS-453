# Module10.py
# CS 453
# Written by Zainab Akinjobi
# Date written : 29th of April. 2021
# Date /time last modified : 29th of Apr. 2021 / 6pm
# Purpose : This program tests different string functions
# Input: Strings

# remove_punc function
def remove_punc(s):        #define the function remove_punc and pass an argument.
    result = ""            #assign empty space to result
    spaces = ["\t", "\n"]  #define the function space
    s = s.strip() #striping whitepsace
    for ii in s:           #using for loop
        
        if ii.isalnum() == True or ii.isspace() == True or ii in spaces: # using an if statement
            result = result + str(ii)  #concatenating result and the string
    return(result)                 #return the new elements in result

# word_count function
def word_count(s): #define the function word_count and pass the arguments
    word_list = s.split(" ") #split the words in word_list when there are spaces
    return(len(word_list))   #return the number of words_list

def add_unique(s, word_list): #define the function add_unique and pass the arguments, word_list
    s_split = s.split(" ") #split the words in s_split
    for word in s_split:  #Using a for loop
        if word not in word_list: #Using an if statement 
            word_list.append(word.lower()) #append wordlist to word and covert the words to lowercase

# remove non-alphanumeric function
def  remove_non_alpha(s):
    result = ""            #assign empty space to result
    for ii in s:           #using a for loop
        if ii.isalnum() == True and ii.isdigit() == False: # using an if statement to return just alphabet
            result = result + str(ii)  #concatenating result and the string
    return(result)               
   
    #  string that contains only letters
def letter_frequency(param):
    param = param.lower()   #convert the string to lower case
    alphabets = []
    letter_count = [0 for  i in range(26)]       #Using a list of integers to tally the number of times each letter that occurs in the string
    for i in range(ord('a'), ord('z')+1):
        alphabets.append(chr(i))   # returns the character associated with the Unicode value
    for letter in param:
        if(letter.isalpha() == True):      #using an if statement to check if it is an alphabet
            index = alphabets.index(letter)
            letter_count[index] = letter_count[index] + 1
    return(letter_count)

def main(): #writing statements to test functions
    
    # Testing remove_punc
    print("Testing remove_punc function ")
    print()
    myString_1 = input('Type something with punctuation: ') # Taking input
    newString_1 = remove_punc( myString_1 ) # passing input to remove_punc function; call remove_punc
    print()
    print('Here is the string without punctuation: ', newString_1) # Displaying the input string without any punctuation
    print()
    
    
    # Testing word_count
    print("Testing word_count function")
    print()
    print("The number of words in the entered string without punctuation is: ", word_count(newString_1)) # Counting the number of words in user input after removing punctuation
    print()
    
    
    # Testing add_unique
    print("Testing add_unique function")
    print()
    word_list_1 = "This is where you will write statements to test the 3 functions above".split(" ") # making up an initial word list
    print("Initial word list is: ", word_list_1) # Displaying the initial word list
    print()
    add_unique(newString_1, word_list_1) # passing the user input without punctuation to add_unique for addition to the word list recently created
    print("New word_list is: ", word_list_1) # displaying the new word list
    
 # Testing remove_non_alpha
    print("Testing remove_non_alpha function")
    print()
    word_list_1 = "This is where you will write statements. Try writing a correct statement: to test the 3 functions above" # making up an word
    print("The result after removing all non alphanumerics: ", remove_non_alpha(word_list_1)) # Displaying the initial word list with all non alphanumeric removed
    print()

 # Testing letter_frequency
    print("Testing letter_frequency function")
    print()
    word_list_2 = "This is where you will write statements. Try writing a correct statement: to test the 3 functions above" # making up an word
    print("The list of letter count is below")
    print(letter_frequency(word_list_2)) # Displaying the word count list
    print()
        
    
if __name__ == '__main__':
 # call the main function
    main( )












