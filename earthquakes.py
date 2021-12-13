# earthquakes.py
# CS 453
# Written by Zainab Akinjobi
# Date written : 6th of May. 2021
# Date /time last modified : 6th of May. 2021 / 6pm
# Purpose : This program tests different string functions
# Input: Make plot from input file


# importing os and matplotlib module
import os

import matplotlib.pyplot as plt


def main():
    # setting input file name
    input_file1 = "earthquake_data.txt"
    # checking if file exist
    if(os.path.exists(input_file1)):
        # opeining file  
        my_file1 = open(input_file1,'r')
        # creating empty list for years
        years = []
        # creating empty list for earthquakes
        earthquakes = []
        # looping through file
        for line in my_file1:
            # splitting the line at space
            list1 = line.split()
            # adding to the list of years
            years.append(int(list1[0]))
            # adding to the list of earthquakes
            earthquakes.append(int(list1[1]))
        # closing file        
        my_file1.close()
        # making the plot
        plt.plot(years, earthquakes, color = "green")
        # adding x label
        plt.xlabel("Years")
        # adding y label
        plt.ylabel( 'Number of Earthquakes\n(Magnitude > 7)')
        # adding title
        plt.title('Strong Earthquakes in the 1900\'s')
        # adding grid
        plt.grid()
        # year list
        int_list = list( range(1900, 2001, 20) )
        # string of year list
        str_list = [ str(i) for i in int_list]
        # adding ticks
        plt.xticks(int_list, str_list)
        # get max of earthquakes
        max_quakes = max(earthquakes)  
        # get year with max earthquakes
        max_year = years[earthquakes.index(max_quakes)]
        # add annotation to the plot with the max of earthquake and year
        plt.annotate("High of " + str(max_quakes) + " in " + str(max_year), xy = (max_year, max_quakes), xytext = (max_year + 2, max_quakes ))
        # show plot
        plt.show()

    else:
        # display error if file does not exist
        print('Error: The file does not exist.')


# calling the main function       
if __name__ == '__main__':
   # call the main function
   main( )       
        

