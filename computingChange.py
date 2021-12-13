# -*- coding: utf-8 -*-

# computingChange.py
# CS 153 or 453
# Written by Zainab Akinjobi
# Date written 2/11/2021
# Date/time last modified 2/11/2021/8am
# Purpose: This program calculates the number of bills needed to give change.
# Input: amount of change to give in dollars
# Output: number of bills (twenties, tens, fives, and ones)

amount_to_change = int(input("Enter the amount to change: ")) #taking input from user

num_twenties = amount_to_change // 20 # calculating number of twenties
remainder = amount_to_change % 20 # remaining change after calculating number of twenties

num_tens = remainder// 10 # calculating number of tens
remainder = remainder % 10 # remaining change after calculating number of tens


num_fives = remainder // 5 # calculating number of fives
num_ones = remainder % 5 # calculating number of ones

print('Change for $', amount_to_change)

print(num_twenties, 'twenty dollar bill(s) and', num_tens, 'ten dollar bill(s)') # output number of tens and twenties

print(num_fives, 'five dollar bill(s) and', num_ones, 'one dollar bill(s)')  # output number of fives and ones
