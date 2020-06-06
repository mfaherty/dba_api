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
import pandas as pd


#url to scrap

url='https://www.worldometers.info/coronavirus/#countries'
#url= 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'
# url=' https://www.worldometers.info/coronavirus/coronavirus-death-toll/'

#Function to run requests.get. and get data from url. use BS4 to return html data 
r = requests.get(url).text
soup = BeautifulSoup(r,'html.parser')
# print(soup)

 # parse html 
    
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
    

#print(final)
#print(type(final))

# Write to a csv file.     

with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, sys.stdout, lineterminator='\n') # removing blank lines from output. 
        writer.writerow(["Index", "Country", "Total Cases", "New Cases", "Total Deaths", "New Deaths", "Total Recovered", "Active Cases", "Serious Critical"," ",  "Tot Cases/1M pop", "Deaths/1M pop", "Total Tests", "Tests/1M pop", "population"]) 
        writer.writerows(output_rows)

# 
# Annoyingly there are a number of extra entries, to do with continents, Not necessary, but they look messy. 
# Cleaning up the output.         
# Create a Dataframe from CSV, read in the output file and drop the toplines 1 to 8. 
coviddata = pd.read_csv('output.csv', encoding = "ISO-8859-1", skiprows=[1,2,3,4,5,6,7,8], engine='python')

coviddata.to_csv('output2.csv', encoding='utf-8')