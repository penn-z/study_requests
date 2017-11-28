#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup


html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html.read(), 'lxml')

# nameList = bsObj.find_all("span", {"class": "green"})
# for name in nameList:
#     print(name.get_text())


# test param text
nameList = bsObj.find_all(text="the prince") # 查找text文本内容为the prince的标签
# print(len(nameList)) # 7

# test param keyword
allText = bsObj.find_all(id="text")
print(allText[0].get_text())
