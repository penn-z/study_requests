#!/usr/bin/env python3
#-*- conding: utf-8 -*-
from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import datetime
import random
import re

random.seed(datetime.datetime.now())
def getLinks(wordUrl):
    try:
        html = urlopen("https://en.wikipedia.org" + wordUrl)
    except (HTTPError, URLError) as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), 'lxml')
        links = bsObj.find("div", {"id": "bodyContent"}).find_all(
            "a", href=re.compile("^(\/wiki\/)((?!:)).*"))
    except AttributeError as e:
        return None
    return links

step = 0
start_url = "/wiki/Kevin_Bacon"
links = getLinks(start_url)
while len(links) > 0 and step < 10:
    step += 1
    newWordUrl = links[random.randint(0, len(links) - 1)].attrs["href"] # 随机取出其中一个链接
    print(newWordUrl)
    print(step)
    links = getLinks(newWordUrl)
