#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup

num = 0  # 循环第几本书籍
url = 'http://books.toscrape.com/catalogue/category/books/travel_2/index.html'
res = requests.get(url)
result = res.text
soup = BeautifulSoup(result,'html.parser')
list = soup.find_all('li',class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")
#书籍价格
for product in list:
	price = product.find_all(class_="product_price")
	for pod in price:
		price_color = pod.find_all(class_="price_color")
		for pow in price_color:
			print('书籍的价格是：'+pow.text)
# #书籍评分---
for rating in list:
	star_rating = rating.find_all(class_="star-rating")
	#print(type(star_rating))
	for stars in star_rating[0:1]:
		star = stars['class'][1:]
		for xingxing in star:
			num = num + 1
			print('第'+str(num)+'书籍的评分是：'+xingxing)
# #书籍名称
for names in list:
	name = names.find_all('a')
	for Name in name[1:]:
		#print(Name['title'])
		print('书籍名称是：'+Name['title'])


