# word.py
# CS 453
# Written by Zainab Akinjobi
# Date written 4th of March 2021
# Date/time last modified 4th of March 2021/ 8:00pm
# Purpose: To use the if statement with correct indentation
# Input: List of words
# Output: seperate long words from short words in an entered string

''' create an empty list named short_words '''
short_words= []

''' create an empty list named long_words '''
long_words= []

for x in range(10):
    
    ''' input a string (use a prompt) and store it in a variable called word '''
    
    word=input('Enter a string: ')
 
    ''' Note: You must use an if-else statement. '''
    ''' if the word is 5 letters or less, append it to short_words,
 otherwise append it to long_words '''
 
    if len(word) <= 5:
        short_words.append(word)
    else:
         long_words.append(word)
         
# the loop is over, move all the way back to the left edge

''' print a message that says how many short words there were '''
print('\nThere are {} shortwords'.format(len(short_words)))
      
''' print the short_words list '''

print('The list of short words are : ', short_words)

''' print a message that says how many long words there were '''

print('\nThere are {} short words'.format(len(long_words)))

''' print the long_words list '''
print('There lists of long words are {}'.format(long_words))