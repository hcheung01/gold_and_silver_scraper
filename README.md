# Gold and Silver historical fetcher
---
## Description
This project is about webscraping, saving, and statiscally analyzing data:

## How does it work?

### Please edit your local path on line #1 in each file to python3 interpreter
example: `#!/usr/bin/python3` or `#!/usr/local/bin/python3`

### fetcher_prices file
This program will parse latest historical 1 month dates and prices of gold and silver from a `www.investing.com`. CSV files will be create locally with the extracted data.

To run if path is same or if you will edit the file:
`./fetch_prices.py`

To run without editing path to python3 in the file:
`python3 fetch_prices.py`


### getCommondityPrice file
This program will open previously created CSV files based on your inputs and will return pricing mean and variance of user inputted range of dates. 

Important: 
* Edge cases is implemented, please try different invalid inputs. 
* File is executable
  
This program takes 3 additional input. Date format is year-month-day starting from most recent. For the last input please pick only one type. 
`./getCommodityPrice.py startdate enddate {gold|silver}`

Example:
`./getCommodityPrice.py 2019-04-21 2019-03-28 gold`

## What I used to build this
Python3 with bs4/BeautifulSoup & statistics modules

## Files
---
File|Task
---|---
fetch_prices.py | webscraper and file creator
getCommodityPrice.py | file reader and data statistical analyzer

## Directories
---
Directory Name | Description
---|---
/BigData | Main folder holding all files. New files will be created

## Author
Heindrick Cheung
