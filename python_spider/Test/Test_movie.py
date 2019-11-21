#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup
#序号/电影名/评分/推荐语/链接

url_list = []
num_temp = 0 #电影条数
while num_temp < 250:
	url = 'https://movie.douban.com/top250?start=' + str(num_temp) + '&filter='
	url_list.append(url)
	num_temp = num_temp + 25
	for url_temp in url_list:
		res = requests.get(url_temp)
		bs_movies = BeautifulSoup(res.text,'html.parser')
		bs_movies_list = bs_movies.find_all('ol',class_='grid_view')
		for i in bs_movies_list[0].find_all('li'):
			try:
				#查找序号
				num = i.find('em',class_="").text
				#print(num)
				#查找电影名
				titles = i.find('span',class_="title").text
				#查找推荐语
				tes = i.find('span',class_="inq").text
				#查找评分
				comment = i.find(class_="rating_num").text
				# 查找链接
				url_movie = i.find('a')['href']
				print('序号:' + num + '\n' + '电影名:' + titles + '\n' + '评分:' + comment + '\n' + '推荐语：' + tes +'\n' +'电影链接'+ url_movie)
			except(AttributeError):
				tes = '\n\n'




