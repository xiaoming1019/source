#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup

url = 'http://www.xiachufang.com/explore/'
res_foods = requests.get(url)
result = res_foods.text
bs_foods = BeautifulSoup(result,'html.parser')
list_foods= bs_foods.find_all('div',class_='info pure-u')
list_all = []
for food in list_foods:
	tag_a = food.find('a')
	name = tag_a.text[17:-13]
	url = 'http://www.xiachufang.com'+tag_a['href']
	tag_p = food.find('p', class_='ing ellipsis')
	ingredients = tag_p.text.replace('','')
	list_all.append([name,url,ingredients])
for list in list_all:
	print(list)
#提取食物的url
# for foods_url in list_foods:
# 	food_url = foods_url.find_all('a')
# 	for tag_a in food_url:
# 		print('http://www.xiachufang.com'+tag_a['href'])
# # 提取食物名称
# for list_food in list_foods:
# 	foods = list_food.find_all('p',class_='name')
# 	for food in foods:
# 		food_name = food.text.replace('\n','')
# 		print(food_name.replace(' ',''))
# #提取食料
# for ellipsis in list_foods:
# 	ing = ellipsis.find_all('p',class_='ing ellipsis')
# 	for ing_ellipsis in ing:
# 		print(ing_ellipsis.text.replace('\n',''))







