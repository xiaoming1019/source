#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
# 引用requests模块
for num in range(5):
	res_comments = requests.get('https://c.y.qq.com/base/fcgi-bin/fcg_global_comment_h5.fcg?g_tk=133877995&loginUin=1004613089&hostUin=0&format=json&inCharset=utf8&outCharset=GB2312&notice=0&platform=yqq.json&needNewCode=0&cid=205360772&reqtype=2&biztype=1&topid=102065756&cmd=6&needmusiccrit=0&pagenum='+str(num)+'&pagesize=15&lasthotcommentid=song_102065756_34536033_1471101184&domain=qq.com&ct=24&cv=10101010')
	# 调用get方法，下载评论列表
	json_comments = res_comments.json()
	# 使用json()方法，将response对象，转为列表/字典
	list_comments = json_comments['comment']['commentlist']
	# 一层一层地取字典，获取评论列表
	for comment in list_comments:
	# list_comments是一个列表，comment是它里面的元素
		print(comment['rootcommentcontent'])
		# 输出评论
		print('-----------------------------------')
		# 将不同的评论分隔开来



