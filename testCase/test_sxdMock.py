#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @time 2018/4/1 18:19
# @autor:shangxudong
# @name: test_sxdMock.py
# @software: PyCharm

import unittest
import requests
from unittest.mock import Mock
from unittest.mock import MagicMock
from unittest.mock import patch
from test_sxdSession import test_sxdSession
import test_sxdGetParams
import  test_getDemo
from test_getDemo import test_getDemo
#
# class Counts():
#      def return_add(self,a,b):
#          return a+b
#
#
# class test_SxdMock(unittest.TestCase):
#     def setUp(self):
#         pass
#
#     @patch('test_sxdGetParams.Test_SxdGetParams')
#     @mock.patch.object(test_sxdSession,"add")
#     def test_SxdMock(self,add1,add2):
#         test_sxdGetParams.Test_SxdGetParams()
#         add2.return_value = 13
#         result = test_sxdSession.add(3,4)
#         print(result)
#         self.assertEqual(result,7)
#
#
#
#
#     def tearDown(self):
#         pass
#
# if __name__ == '__main__':
#     unittest.main
# mock值赋给方法
testgetdemo = test_getDemo()
testgetdemo.test_getNoParams = MagicMock(return_value=3)
# print(testgetdemo.test_getNoParams())
# assert testgetdemo.test_getNoParams() == 4
mocks = Mock()
mocks()
print(mocks.assert_called_with())
print(mocks.assert_called())
def sideMethod(arg):
    return len(arg)

mocks.side_effect = sideMethod
print(mocks("sxd"))

@patch('test_getDemo.test_getDemo')
def test(mockcalss):
    assert mockcalss is test_getDemo.test_getDemo
    assert mockcalss.called

with patch.object(test_getDemo,'test_getNoParams',return_value = 200) as mockmethod:
     testgetdemo = test_getDemo()
     a  = testgetdemo.test_getNoParams()
     print(a)
     print(mockmethod.assert_called_with())


dict = {"key":"value"}
with patch.dict(dict,{"newkey":"newValue"},clear = True):
    assert dict == {"key":"value"}

