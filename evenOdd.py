# word.py
# CS 453
# Written by Zainab Akinjobi
# Date written 4th of March 2021
# Date/time last modified 4th of March 2021/ 9:00pm
# Purpose: To use the if statement with correct indentation to diffrentiate between even and odd numbers
# Input: List of numbers
# Output: seperate even numbers from odd numbers

''' create an empty list named even_numbers '''
even_numbers =[]

''' create an empty list named odd_numbers '''
odd_numbers = []

for x in range(10):
    
    ''' input an integer (use a prompt) and store it in a variable called number '''
    number = int(input('Enter an integer : '))
    ''' Note: You must use two distinct if statements. '''
 
    ''' if the number is even, append it to the even_numbers list '''
    if number % 2 == 0:
        even_numbers.append(number)    
 
    ''' if the number is odd, append it to the odd_numbers list '''
    if number % 2 != 0:
        odd_numbers.append(number)
        
# the loop is over, move all the way back to the left edge
''' print a message that says how many even numbers there were '''
print('\nThe even numbers are {} in total'.format(len(even_numbers)))

''' print the even_numbers list '''
print('\nThe list of even numbers : {},'.format(even_numbers))

''' print a message that says how many odd numbers there were '''
print('\nThe odd numbers are {} in total'.format(len(odd_numbers)))

''' print the odd_numbers list '''
print('\nThe list of odd numbers : {}'.format(odd_numbers))



