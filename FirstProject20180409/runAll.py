#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/4/10 15:07
# @author :shangxudong
# @File   : runAll.py
# @Software: PyCharm Community Edition
import unittest
import test_001
from HTMLTestRunner import HTMLTestRunner
import time



# 自动发现用例
test_dir = "./testCase"
discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

if __name__ == '__main__':
    # suit = unittest.TestSuite()
    # suit.addTest("test_001.test_getNoParams")

    now = time.strftime('%H-%M-%S %Y-%m-%d')
    print(now)
    filename = './testResult/'+now+"_result.html"
    print(filename)
    with open(filename,'wb') as fp:
          # runner = unittest.TextTestRunner()
          runner = HTMLTestRunner(stream=fp,title="接口测试",description="测试接口1")
          runner.run(discover)
