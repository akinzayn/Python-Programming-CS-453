
# CS 153 or 453 Zainab Akinjobi
# Written by Zainab Akinjobi
# Date written 03/10/2021
# Date/time last modified 03/10/2021 10:30 pm
# Purpose:Solve loop problems

# Write a for loop to print the lowercase letters 'a' through 'z', one character per line.
print()
print('Problem 0ne')

for ii in range(97, 123):
    print(chr(ii))
print()
    

# Nested for loops to display a triangle made of asterisks.
print()     
print('Problem Two')
user_input = int(input('Enter a number: '))
if user_input <1 or user_input>50 :
    print('Invalid input')
else:
    for ii in range (user_input,0,-1):
        print(str(ii * '*').rjust(user_input))
print()

# Counting the number of vowela in string entered by user

print()        
print('Problem Three')  
user_input =input ('Enter a string: ')  
user_input = user_input.lower()
 
(a,e,i,o,u)=(0,0,0,0,0)
vowel_tuple = (a,e,i,o,u)
vowels= ['a','e','i','o','u']  
for count in user_input:
    if count == 'a':
        a=a+1
    elif count == 'e':
        e= e+1
    elif count =='i':
        i=i+1
    elif count =='o':
        o=o+1
    elif count == 'u':
        u=u+1
    else:
         continue
vowel_tuple = (a,e,i,o,u)
for ii in range(len(vowels)) :
    print("# of {}'s: {:3d}".format(vowels[ii],vowel_tuple[ii]))
print()    

# Sorting a list of words from user 
print()
print('Problem 4') 
user_input = input("Enter a word: ")

word_list = []
while user_input.lower() != "quit":
    to_add = True
    ii = 0
    while ii <= (len(user_input) - 1):
        if ' ' == user_input[ii]:
            to_add = False
        ii = ii + 1
    if to_add == True:
        word_list.append(user_input) 
    user_input = input("Enter a word: ")   
word_list.sort()    
for word in word_list:
    print(word)
print()
    

   
              
    
                  
             
             
            
        
    
        
        
    
    


