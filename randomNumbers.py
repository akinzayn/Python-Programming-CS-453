# CS 153 or 453 Zainab Akinjobi
# Written by Zainab Akinjobi
# Date written 03/10/2021
# Date/time last modified 03/10/2021 10:30 pm
# Purpose:Generating random numbers and alingning them 


import random # importing the random module

num_list  = [] # create an empty list

# for loop to generate 100 random number
for ii in range(100):
    num_list.append(random.randint(1, 1000)) # appending the list with a generated random number

# priinting the list nicely
for count in range(100):
    end = " "  # Initializing the end argument
    if (count+1) % 10 == 0: # checking if 10 numbers have been printed
        end = '\n'
    print("{:5d}".format(num_list[count]), end = end) # printing number




