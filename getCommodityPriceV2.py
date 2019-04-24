#!/usr/local/bin/python3
"""
statistical gold/silver prices with user inputted dates
"""
from statistics import mean, variance
from datetime import datetime
from sys import argv
import csv
import os
"""
Object-orient way for more modular opproach and Unittesting
"""

class Calc_prices():
    data = {}
    final_list = []

    def __init__(self, start, end, type):
        self.start = start
        self.end = end
        self.type = type + "_" + str(datetime.now().date()) + ".csv"
       
    def open_file(self):
        file = self.type
        with open(file, 'r') as csv_file:
            csv_data = csv.reader(csv_file, delimiter='|')

            for row in csv_data:
                full_date = str(datetime.strptime(row[0], '%b %d, %Y'))[:10]
                Calc_prices.data[full_date] = float(row[1].replace(',', ''))

            return Calc_prices.data

    def slice(self):
        counter = 0
        for key in Calc_prices.data.keys():
            if key == self.start:
                start = counter
            if key == self.end:
                 break
            counter += 1
        Calc_prices.final_list = list(Calc_prices.data.values())[start:]
        return Calc_prices.final_list

    def mean(self):
        return mean(Calc_prices.final_list)

    def variance(self):
        return variance(Calc_prices.final_list)
    


if __name__ == "__main__":
    commondity_obj = Calc_prices(argv[1], argv[2], argv[3])
    data_dict = commondity_obj.open_file()
    final_list = commondity_obj.slice()
    mean = commondity_obj.mean()
    variance = commondity_obj.variance()

    if mean and variance and argv[3]:
        print("{} {:.2f} {:.2f}".format(argv[3], mean, variance))
    else:
        print('Invalid input')

# can add unittest here, I will probably do another version with Unittesting