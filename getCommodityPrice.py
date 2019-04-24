#!/usr/local/bin/python3
"""
calculate mean and variance of gold/silver prices with user inputted range of dates
"""
from statistics import mean, variance
from datetime import datetime
from sys import argv
import csv
import os

def calc_prices():

    if len(argv) == 4:
        start_date = argv[1]
        end_date = argv[2]
        file_name = argv[3] + "_" + str(datetime.now().date()) + ".csv"

        # Check if length of start/end dates is correct and if file exists 
        if len(start_date) == 8 and len(end_date) == 8 and os.path.exists(file_name):

            # Open existing CSV file
            with open(file_name, 'r') as csv_file:

                # Save all prices to list while keeping track of starting/ending index of prices
                range_list = []
                ct = 0
                csv_reader = csv.reader(csv_file, delimiter='|')
                for row in csv_reader:
                    full_date = str(datetime.strptime(row[0], '%b %d, %Y'))
                    converted_date = full_date[5:10] + '-' + full_date[2:4]
                    if start_date == converted_date:
                        start = ct
                    if end_date == converted_date:
                        end = ct
                    range_list.append(float(row[1].replace(',', '')))
                    ct += 1
                try:
                    # if both index exist, slice needed range of prices from list 
                    range_list = range_list[start:end + 1]

                    # find mean and variance from list of pricing and return formatted tuple
                    print("{} {:.2f} {:.2f}".format(argv[3], mean(range_list), variance(range_list)))
                except:
                    print("Invalid, something is wrong with the dates")
        else:
            print("Invalid, please make sure to input correct dates and commodity type")
    else:
        print('Missing input(s)')



if __name__ == "__main__":
    calc_prices()

