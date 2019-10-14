#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

import time
import unittest
from selenium import webdriver

class TestLogin(unittest.TestCase):
    # 指定浏览器
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 打开url
        self.driver.get('https://ts.i-lz.cn/login')

    # 登录操作
    def test_login(self):
        title = self.driver.title
        print(title)
        now_url = self.driver.current_url
        print(now_url)
        username = 'lzkj'
        password = 'lzhd6688'

        # 执行登录操作
        # 定位用户名输入框，并输入用户名
        self.driver.find_element_by_id("login").clear()
        self.driver.find_element_by_id("login").send_keys(username)
        # 定位密码输入框，并输入密码
        self.driver.find_element_by_id("pwd").clear()
        self.driver.find_element_by_id("pwd").send_keys(password)
        # 点击登录操作
        self.driver.find_element_by_class_name("login_fields__submit").click()
        # 休息5s
        time.sleep(5)


    # 关闭浏览器
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()













