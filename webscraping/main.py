# -*- coding: utf-8 -*-
"""
Created on Sat Oct 14 01:55:26 2023

@author: c.samanja09
"""

from bs4 import BeautifulSoup

with open('home.html','r') as html_file:
    content= html_file.read() 

    soup=BeautifulSoup(content,'lxml')
    print(soup.prettify())       
    print(content)