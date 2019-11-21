#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

from MyQR import myqr
import os

version, level, qr_name = myqr.run(
	words = 'https://www.baidu.com',
	version = 1,
	level = 'H',
	picture = 'baby.jpg',
	colorized = True,
	contrast = 1.0,
	brightness = 1.0,
	save_name = 'baby_2.jpg',
	save_dir = os.getcwd()
)