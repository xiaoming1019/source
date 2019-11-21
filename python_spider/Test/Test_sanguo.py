#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup

url = 'https://wordpress-edu-3autumn.localprod.oc.forchange.cn/all-about-the-future_04/'
res = requests.get(url)
html = res.text
soup = BeautifulSoup(html,'html.parser')
pinglun = soup.find(class_='comments-area')
PingLing = pinglun.find_all(class_='comment byuser comment-author-spiderman even thread-even depth-1')
for pl in PingLing:
	xm = pl.find_all('div',class_='comment-content')
	for xx in xm:
		xp = xx.find('p')
		print(xp.text)

