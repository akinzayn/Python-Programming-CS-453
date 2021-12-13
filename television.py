# -*- coding: utf-8 -*-

# computingChange.py
# CS 153 or 453
# Written by Zainab Akinjobi
# Date written 2/11/2021
# Date/time last modified 2/11/2021/11am
# Purpose: This program calculates the width and height of a Television.
# Input: the diagonal measurement of the television in inches.
# Output:  the width and height of the television screen

import math

diagonal = float(input('Enter the diagonal of the television in inches : '))

width = (diagonal/math.sqrt(16**2 + 9**2)) * 16 # Computing width of television

height = 9/16 * width # Computing height of television

print('The width is ', width)
print('The height is ', height )
