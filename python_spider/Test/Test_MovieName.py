#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
from bs4 import BeautifulSoup
from urllib.request import quote

movie_name = input('输入你想看的电影名字：')
movie_name_gbk = movie_name.encode('gbk')
url = 'http://s.ygdy8.com/plus/so.php?typeid=1&keyword='+quote(movie_name_gbk)
# print(url)
res = requests.post(url)
soup = BeautifulSoup(res.text,'html.parser')
soup_ul = soup.find_all('ul')
for soup_i in soup_ul:
	soup_tr = soup_i.find_all('tr',height="24")
	for soup_url in soup_tr:
		soup_url_1 = soup_url.find('a')['href'] #获取下载页面的后连接后半段
		# 下载页面
		Down_url = 'http://s.ygdy8.com' + soup_url_1
		Down_res = requests.post(Down_url)
		Down_soup = BeautifulSoup(Down_res.text,'html.parser')
		Down_soup_all = Down_soup.find_all('tbody')
		for Down_soup_i in Down_soup_all:
			Down_soup_url = Down_soup_i.find('a')['href']
			print('下载链接：'+ Down_soup_url)


