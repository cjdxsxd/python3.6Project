#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @time 2018/4/1 17:46
# @autor:shangxudong
# @name: test_sxdGetParams.py
# @software: PyCharm
import unittest
import requests

class Test_SxdGetParams(unittest.TestCase):

    def setUp(self):
        pass


    def testGetParams(self):

        # headers = {"key1":"values1"}
        params = {"key2":"value2"}
        r = requests.get(url="http://httpbin.org/get",params=params)
        print(r.text)

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main