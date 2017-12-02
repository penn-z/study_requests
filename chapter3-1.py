#!/usr/bin/env python3
#-*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen("https://en.wikipedia.org/wiki/Kevin_Bacon")
bsObj = BeautifulSoup(html.read(), 'lxml')
# for link in bsObj.find_all("a"):
#     if 'href' in link.attrs:
#         print(link.attrs['href'])

content = bsObj.find("div", {"id": "bodyContent"})
# print(content)

for link in bsObj.find("div", {"id": "bodyContent"}).find_all("a", 
                        href=re.compile("^\/wiki\/(?!:).*")):
    if "href" in link.attrs:
        print(link.attrs["href"])
