#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import requests
from PIL import Image
from io import BytesIO

# r = requests.get('https://api.github.com/events')
# print(r.encoding)
# r.encoding = 'utf-8'
# print(r.content)
# i = Image.open(r.text)
# i = Image.open(BytesIO(r.content))

url = 'http://httpbin.org/post'
files = {'file': open('./calendar1.php', 'rb')}
u = requests.post(url, files=files)
print(u.text)
