#!/usr/local/bin/python3
"""
Webscraper for gold/silver dates and prices
"""
from bs4 import BeautifulSoup
from datetime import datetime
import requests
import csv


def request_page(url):
    """GET request for gold/silver date"""

    page = requests.get(url, headers={'User-Agent': 'Candidate'})
    if page.status_code is 200:
        return page
    return None

def get_table_data(request_obj):
    """Get table data from request object"""

    # parse html and return table only
    table = BeautifulSoup(request_obj.text, 'html.parser').find(
        'div', attrs={'id': 'results_box'}).find('tbody').find_all('tr')
    return table


def save_to_csv(table, title):
    """Save dates and prices to CSV file"""

    # save to CSV in local directory, file name will be formatted as: commodity type + date
    with open(title + "_" + str(datetime.now().date()) + ".csv", 'a') as csv_file:
        for arg in table:
            data = arg.find_all('td')
            # only the first and second element is needed and don't have to worry about different classnames
            todays_date = data[0].text
            todays_price = data[1].text

            # set delimiter to | for future read/compare conflicts since date and prices have commas already
            writer = csv.writer(csv_file, delimiter='|')
            writer.writerow([todays_date, todays_price])


def fetch_data():
    """primary method to scrape gold and silver data from static page"""

    gold_url = "https://www.investing.com/commodities/gold-historical-data"
    silver_url = "https://www.investing.com/commodities/silver-historical-data"

    gold_request = request_page(gold_url)
    silver_request = request_page(silver_url)
    if not gold_request or not silver_request:
        return None

    gold_table = get_table_data(gold_request)
    silver_table = get_table_data(silver_request)

    # check if tables is extracted, if call save method with commodity type 
    if gold_table: 
        save_to_csv(gold_table, 'gold')
    if silver_table:
        save_to_csv(silver_table, 'silver')


if __name__ == "__main__":
    # I can expand method to take in url as parameters from command line
    fetch_data()
