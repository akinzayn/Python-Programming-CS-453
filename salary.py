# -*- coding: utf-8 -*-
# salary.py
# CS 453
# Written by Zainab Akinjobi
# Date written : 4th of Feb. 2021
# Date /time last modified : 4th of Feb. 2021 / 6pm
# Purpose : This program does salary calculations.
# Input:the person's hourly wage
# Output : the person's annual salary and monthly salary

hourly_wage = float(input('Enter hourly wage :'))

print('Annual salary is :')
print (hourly_wage * 40 * 50)
print ()

print ('Monthly salary is:')
print(((hourly_wage * 40 * 50) /12))
print()


