# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 01:55:26 2023

@author: c.samanja09
"""

from bs4 import BeautifulSoup

import requests

html_text=requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=Python&txtLocation=').text
soup = BeautifulSoup(html_text,'lxml')
job=soup.find_all('li',class_='clearfix job-bx wht-shd-bx')
