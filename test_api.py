# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 14:55:35 2020

@author: maryf
"""


# Importing libraries needed.


from unittest import TestCase
import api2
import requests
  
from bs4 import BeautifulSoup
import requests


class Api(object):
    
    def getdata(self):
        url= 'https://www.worldometers.info/coronavirus/countries-where-coronavirus-has-spread/'

        #Function to run requests.get. and get data from url. use BS4 to return html data 
        r = requests.get(url).text
        soup = BeautifulSoup(r,'html.parser')
 
    

# test the Api functionality
class TestApi(unittest.TestCase):

    def setUp(self):
        self.api = Api()
        
        
    def test_getdata(self):
        response = requests.get(url)
        response.status_code == 200    # There is a reponse from url
        assert len(str(response)) > 0 # data is returned.
        

if __name__ == '__main__':
    unittest.main()
