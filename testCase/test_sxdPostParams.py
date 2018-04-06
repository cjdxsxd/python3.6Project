#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @time 2018/4/1 17:52
# @autor:shangxudong
# @name: test_sxdPostParams.py
# @software: PyCharm

import unittest
import requests
import json


class text_sxdPostParams(unittest.TestCase):

    def setUp(self):
        pass

    def test_sxdPostParams(self):
        # 表单形式提交
        data = {"key3":"value3"}
        #非表单形式(字典转换成json)
        r = requests.post("http://httpbin.org/post",data=json.dumps(data))
        print(r.text)
        print(r.json())

    def tearDown(self):
        pass