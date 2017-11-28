#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html.read(), 'lxml')
images = bsObj.find_all("img", {"src": re.compile("\.\.\/img\/gifts\/img.*\.jpg")})
for image in images:
    print(image["src"])
