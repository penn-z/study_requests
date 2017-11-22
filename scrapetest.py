#!/bin/bash/evn python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
# html = urlopen("http://pythonscraping.com/pages/page1.html")
# print(html.read())
# bsObj = BeautifulSoup(html.read(), 'lxml')
# print(bsObj.html.body.h1)

try:
    html = urlopen("http://pythonscraping.com/pages/page1.html")
    # html = urlopen("http://pythonscraping.com")
    bsObj = BeautifulSoup(html.read(), 'lxml')
    # print(bsObj.html.h1)
    badContent = bsObj.nonExisting.anotherTag
except HTTPError as e:
    print(e)
except AttributeError as e:
    print("Tag was not found")
else:
    if badContent == None:
        print('URL is not found')
    else:
        print(badContent)
