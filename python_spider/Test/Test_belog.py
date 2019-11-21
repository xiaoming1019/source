#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup

url = 'https://spidermen.cn/'
res = requests.get(url)
result = res.text
soup = BeautifulSoup(result,'html.parser')
head = soup.find_all(class_='entry-header')
for kind in head:
	Total = kind.find_all(class_="entry-title")
	Times = kind.find_all(class_="entry-date published")
	for time in Times:
		print('时间：'+time.text)
	for total in Total:
		# 书籍名称
		txt = total.text
		print('书籍名称：'+txt)
		for bref in total:
			print('书籍链接：'+bref['href'])



