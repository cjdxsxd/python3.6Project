#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @time 2018/4/1 17:19
# @autor:shangxudong
# @name: RunTest.py
# @software: PyCharm

import unittest
from test_getDemo import test_getDemo
# import sys
# print(sys.path)

import logging
logging.basicConfig(level=logging.INFO,format='%(asctime)s-%(name)s-%(levelname)s-%(message)s')

logger = logging.getLogger()
logger.setLevel(level=logging.INFO)
formatter = logging.Formatter('%(asctime)s-%(name)s-%(levelname)s-%(message)s')
handler = logging.FileHandler("D:\\sxdlog.txt")
handler.setLevel(level=logging.INFO)
handler.setFormatter(formatter)
consle = logging.StreamHandler()
consle.setLevel(level=logging.INFO)
consle.setFormatter(formatter)

logger.addHandler(handler)
logger.addHandler(consle)




if __name__ == "__main__":
    suit = unittest.TestSuite()
    # testcase = unittest.TestLoader().loadTestsFromTestCase(test_getDemo)
    # testcase = [test_getDemo("test_getNoParams")]
    # suit.addTests(testcase)
    # suit.addTest(test_getDemo("test_getNoParams"))
    testcase = unittest.defaultTestLoader.discover(start_dir="./",pattern="test*.py")
    suit.addTests(testcase)
    logging.info("消息")
    runner = unittest.TextTestRunner()
    runner.run(suit)