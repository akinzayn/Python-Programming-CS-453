# -*- coding: utf-8 -*-
# salary.py
# CS 453
# Written by Zainab Akinjobi
# Date written : 17th of Feb. 2021
# Date /time last modified : 18th of Feb. 2021 / 6pm
# Purpose : This program creates list variables
# Input: Create empty list
# Output : Print sum of elements, min, max and ave of a list 

myList =[] #create an empty list
user_input1=float(input('Enter a number: ')) #user input a float
user_input2=float(input('Enter a number: ' ))#user input a float
user_input3=float(input('Enter a number: ' ))#user input a float
user_input4=float(input('Enter a number: ' ))#user input a float
user_input5=float(input('Enter a number: ' ))#user input a float

myList.append(user_input1) # Append user input to myList
myList.append(user_input2) # Append user input to myList
myList.append(user_input3) # Append user input to myList
myList.append(user_input4) # Append user input to myList
myList.append(user_input5) # Append user input to myList

sumList= myList[0]+myList[1]+myList[2]+myList[3]+myList[4] #add the elements in myList
minList= min(myList) # The minimum value on myList
maxList= max(myList) # The maximum value on myList
aveList= sumList / 5  # The average of myList
lastList = myList.pop(4) # The last value on myList
print('The sum of the list is ' ,sumList)
print('The minimum value in the list is ' , minList)
print('The maximum value in the list is '  , maxList)
print(' The average of the list is ' , aveList)
print('The last element on the list is ' ,last
      List)