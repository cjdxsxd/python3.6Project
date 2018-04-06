#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @time 2018/3/15 23:47
# @autor:shangxudong
# @name: test_getDemo.py
# @software: PyCharm

import requests
import unittest
import json
class test_getDemo(unittest.TestCase):
    url = "https://httpbin.org/"
    def test_getNoParams(self):
        resp = requests.get(self.url)
        #http响应字符串形式,url对应的页面
        # print (r.text)
        #http响应的cookies
        # print(resp.cookies)
        #方法一：使用requests.utilsjar包转字典
        re = requests.utils.dict_from_cookiejar(resp.cookies)
        # print(re)
        #服务器返回状态
        # print(resp.status_code)
        #服务器响应n内容的编码方式
        # print (resp.encoding)
        #http响应头部内容
        print(resp.headers)
        # print(json.dumps(resp.headers)
        #请求的url
        # print(resp.url)
        #响应内容用json序列化输出，才能用json.否则会报错
        # print(resp.json())

if __name__ == '__main__':
    unittest.main()