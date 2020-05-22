# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:55:35 2020
@author: maryf
"""


# Importing libraries nedded.

from bs4 import BeautifulSoup
import requests
import csv
import unittest 
import sys

#url to scrap

#url= 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
url=' https://www.worldometers.info/coronavirus/coronavirus-death-toll/'

#Function to run requests.get. and get data from url. use BS4 to return html data 
r = requests.get(url).text
soup = BeautifulSoup(r,'html.parser')
# print(soup)


   
    
output_rows = []
for table_row in soup.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    # using list comprehension + enumerate() 
    # removing multiple spaces 
    final = [val for idx, val in enumerate(output_rows) 
       if val or (not val and output_rows[idx - 1])] 
    

print(final)
print(type(final))
    

with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, sys.stdout, lineterminator='\n') # removing blank lines from output. 
        writer.writerow(["Country", "Cases", "Deaths", "Region"]) 
        writer.writerows(output_rows)

