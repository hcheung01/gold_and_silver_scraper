# Gold and Silver historical fetcher
---
## Description

This project is about webscraping, saving, and statiscally analyzing data:

## How does it work?
### fetcher file
This program will parse and extract latest one month historical dates and prices of gold and silver from a website. CSV files will be create locally 

To run if path is same or if you will edit the file:
`./fetch_prices.py`

To run without editing path to python3 in the file:
`python3 fetch_prices.py`


### get commodity price file
This program will open previously created CSV files and find mean/variance of user inputted range of dates. 

Important: Edge cases is implemented, please try different invalid inputs.

To run if path is same or if you will edit the file:
`./getCommodityPrice.py startdate enddate gold|silver`

To run without editing path to python3 in the file:
`python3 getCommodityPrice.py startdate enddate gold|silver`

Example:
`./getCommodityPrice.py 04-17-19 03-21-19 gold`

## Python3/modules
bs4/BeautifulSoup | statistics

## Files
---
File|Task
---|---
fetch_prices.py | webscraper
getCommodityPrice.py | statistic algorithm

## Directories
---
Directory Name | Description
---|---
/BigData | Main folder holding all files

## Author
Heindrick Cheung
