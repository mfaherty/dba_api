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

#url to scrap

url= 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

#Function to run requests.get. and get data from url. use BS4 to return html data 

def getdata(url):
    r = requests.get(url).text

#print(r)
    soup = BeautifulSoup(r,'html.parser')
    return soup

#print(soup)

covid_table = soup.find_all("tr")
print(covid_table)

# Function to search through response r for data in the table.

def search_data():
    output_rows = []
    for table_row in soup.findAll('tr'):
        columns = table_row.findAll('td')
        output_row = []
        for column in columns:
            output_row.append(column.text)
        output_rows.append(output_row)
        #output_rows = [x.strip(' ') for x in output_rows]
        #final=list(map(lambda x:x.strip(),output_rows))
        #print(final)
        return output_rows
    
print(output_rows)
#print(type(final))
    
# function to write the date to an output file. 
def write_function():
    
    with open('output.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Country", "Cases", "Deaths", "Region"]) 
        writer.writerows(output_rows)                            
                              
                              
                              
                              
                    
