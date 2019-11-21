#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import requests
res_music = requests.get('https://c.y.qq.com/soso/fcgi-bin/client_search_cp?ct=24&qqmusic_ver=1298&new_json=1&remoteplace=txt.yqq.song&searchid=60997426243444153&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n=20&w=%E5%91%A8%E6%9D%B0%E4%BC%A6&g_tk=5381&loginUin=0&hostUin=0&format=json&inCharset=utf8&outCharset=utf-8&notice=0&platform=yqq.json&needNewCode=0')
json_music = res_music.json()
list_music = json_music['data']['song']['list']
for music in list_music:
	name = music['name']
	print('歌名：'+name)
	album_name = music['album']['name']
	print('所属专辑：'+album_name)
	time = music['interval']
	print('歌曲时间：'+str(time)+'秒')
	music_href = music['mid']
	print('歌曲链接：https://y.qq.com/n/yqq/song/'+music_href+'.html\n\n')


