#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup

url = 'http://books.toscrape.com/'
res = requests.get(url)
result = res.text
bs = BeautifulSoup(result,'html.parser')
nav = bs.find_all(class_="nav nav-list")
for BookName in nav:
	name = BookName.find_all('a')
	for book in name:
		#print(book['href'])
		bn = book.text.replace('\n','')
		print('书籍名称为：'+bn.replace(' ',''))




