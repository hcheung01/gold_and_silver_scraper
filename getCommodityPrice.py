#!/usr/local/bin/python3
"""
statistical gold/silver prices with user inputted dates
"""
from statistics import mean, variance
from datetime import datetime
from sys import argv
import csv
import os

def calc_prices():
    """method to calculate mean and variance from CSV data"""
    if len(argv) == 4:
        start_date = argv[1]
        end_date = argv[2]
        file_name = argv[3] + "_" + str(datetime.now().date()) + ".csv"

        # Check if length of start/end dates is correct and if file exists 
        if len(start_date) == 10 and len(end_date) == 10 and os.path.exists(file_name):

            # Open existing CSV file
            with open(file_name, 'r') as csv_file:

                # Save all prices to list while keeping track of starting/ending index of prices
                range_list = []
                ct = 0
                csv_reader = csv.reader(csv_file, delimiter='|')
                for row in csv_reader:
                    full_date = str(datetime.strptime(row[0], '%b %d, %Y'))[:10]
                    if start_date == full_date:
                        start = ct
                    if end_date == full_date:
                        end = ct
                    range_list.append(float(row[1].replace(',', '')))
                    ct += 1
                try:
                    # if both index exist, slice needed range of prices from list 
                    range_list = range_list[start:end + 1]

                    # find mean and variance from list of pricing and return formatted tuple
                    print("{} {:.2f} {:.2f}".format(argv[3], mean(range_list), variance(range_list)))
                except:
                    print("Invalid date or out of range")
        else:
            print("Invalid, please make sure to input correct date format and commodity type")
    else:
        print('Missing input(s)')



if __name__ == "__main__":
    calc_prices()

