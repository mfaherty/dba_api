# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:55:35 2020

@author: maryf
"""

from bs4 import BeautifulSoup
import requests
import csv

url= 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'



r = requests.get(url).text

#print(r)

soup = BeautifulSoup(r,'html.parser')

#print(soup)

apitable = soup.find_all("tr")

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
    
#print(output_rows)
#print(type(final))
    
with open('output.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Country", "Cases", "Deaths", "Region"]) 
    writer.writerows(output_rows)                            
                              
                              
                              
                              
                              
'''
allapis = soup.find_all("tr")
l={}
u=list()



    

for i in range(0,len(allapis)):
                    #try:
                    api = allapis[i].find_all("td")
                    #except:
                        #api=None
                    
                    try:
                        l["Country"]=api[0].text.replace("\n","")
                    except:
                        l["api"]=None
                        
                    try:
                        l["Cases"]=api[1].text.replace("\n","")
                    except:
                        l["api"]=None
                        
                    try:
                        l["Deaths"]=api[2].text.replace("\n","")
                    except:
                        l["api"]=None
                        

                    try:
                        l["Region"]=api[2].text.replace("\n","")
                    except:
                        l["api"]=None
                    
                    
                        
                    u.append(l)
                    l={}
                    
                   

## then we open a csv file in append mode
with open("stats.csv", "a") as csv_file:
    writer = csv.writer(csv_file)  
    writer.writerow(["Country", "Cases", "Deaths", "Region"])      

print(u)
print(type(u))
print(l)
print(type(l))
                        
'''                        
