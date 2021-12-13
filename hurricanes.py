# hurricanes.py
# CS 453
# Written by Zainab Akinjobi
# Date written : 5th of May 2021
# Date /time last modified : 6th of May 2021 / 6pm
# Purpose : This program tests different string functions
# Input: Make a bar graph 


# importing os module
import os
# import pyplot from matplot module as plt
import matplotlib.pyplot as plt

# main function
def main():
    # setting input file name
    input_file1 = "hurricane_data.csv"
    # checking if file exist
    if(os.path.exists(input_file1)):
        # opeining file      
        my_file1 = open(input_file1,'r')
        # creating empty list for years
        years = []
        # looping through file
        for line in my_file1:
            # splitting the line at comma
            list1 = line.split(",")
            # adding to the list of years
            years.append(int(list1[1]))

        # closing file        
        my_file1.close()
        # creating the list of first years in a decade
        left = list( range(1900, 1991, 10) )
        #  creating an empty list as height
        height = []
        # iterating over left to tally within decade
        for i in range(len(left)):
            # setting first year in the decade
            first_year = left[i]
            # setting last year in the decade
            last_year = first_year + 10
            # settig tally to zero
            tally = 0
            # iterating over years to tally those wihtin a decade
            for year in years:
                # checking if year falls withing the decade
                if first_year <= year < last_year:
                    # adding one to tally
                    tally += 1
            height.append(tally)
        # ploting bar chart   
        plt.bar(left, height, width = 9)  
        # creating ticks for plot
        left_str = [ "'" + str(i).split("9", 1)[1] for i in left ]
        # adding ticks for plot        
        plt.xticks(left, left_str)
        # adding x lable
        plt.xlabel("Decade")
        # adding y label
        plt.ylabel( 'Number of Hurricanes')
        # adding title
        plt.title('Hurricanes in the 1900\'s by Decade')
        # showing plot
        plt.show()

    else:
        # displayin error if file does not exist
        print('Error: The file does not exist.')

 




# calling the main function       
if __name__ == '__main__':
   # call the main function
   main( )       
        

