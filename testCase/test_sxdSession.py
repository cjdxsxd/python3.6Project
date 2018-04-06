#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @time 2018/4/1 17:57
# @autor:shangxudong
# @name: test_sxdSession.py
# @software: PyCharm

import unittest
import requests


class test_sxdSession(unittest.TestCase):
    def setUp(self):
        pass

    def testSession(self):
        with requests.session() as s:
            s.get("http://httpbin.org/cookies/set/123456/1234567")
            r = s.get("http://httpbin.org/cookies")
            print(r.text)
            cookies = requests.utils.dict_from_cookiejar(r.cookies)
            # print({c.key:c.v
            # alue for c in r.cookies})
            dic = {"1":"2"}
            print(dic)

    def add(self,a,b):
        return self.a+self.b

    def tearDown(self):
        pass

if __name__ == "__main__":
    unittest.main