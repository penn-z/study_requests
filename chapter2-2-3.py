#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://www.pythonscraping.com/pages/page3.html')
bsObj = BeautifulSoup(html.read(), 'lxml')

# .children标签表示子标签(即下一代标签，后代标签则指父标签虾下面所有级别的标签)
for child in bsObj.find("table", {"id": "giftList"}).children:
    # print(child)
    pass

# .descendants标签表示后代标签
for child in bsObj.find("table", {"id": "giftList"}).descendants:
    # print(child)
    pass


# .next_siblings，表示兄弟标签，不把自己当兄弟标签且只能调用后面的兄弟标签
for sibling in bsObj.find("table", {"id": "giftList"}).tr.next_siblings:
    # print(sibling)
    pass


# parent,parents查找父标签
print(bsObj.find("img", {"src": "../img/gifts/img2.jpg"
                        }).parent.previous_sibling.get_text())
