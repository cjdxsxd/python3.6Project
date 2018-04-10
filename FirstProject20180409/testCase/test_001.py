#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/4/10 14:54
# @author :shangxudong
# @File   : test_001.py
# @Software: PyCharm Community Edition
import requests
import unittest
import json


class test_001(unittest.TestCase):
    '''001接口测试用例'''

    def setUp(self):
        '''所有案例只执行一次初始化'''
        self.url = "http://www.baidu.com/"

    def test_getNoParams(self):
        '''不带参数请求'''
        r = requests.get(self.url)
        print(r.status_code)
        print(r.headers)

    def test_getHaveParams(self):
        '''带有参数请求'''
        data = {"key1":"value1"}
        r = requests.get(self.url,params=data)
        print(r.url)
        print(r.headers)

    def tearDown(self):
        pass

if __name__ == '__main__':
    unittest.main()