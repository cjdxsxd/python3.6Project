#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @time 2018/3/24 19:54
# @autor:shangxudong
# @name: test_StrFunctionDemo.py
# @software: PyCharm

# str = "with a moo-moo here,and a moo-moo there"
#
# subString = str.find("moo",13)
#
# print(subString)

# list1 = ['1','2','3','4','5']
# seq = "+"
# strJoin = seq.join(list1)
# print(strJoin)

# str = "this is a book"
# str2 = str.replace("is","IS")
# print(str2)

# str = "1+2+3"
# str1 = str.split("+")
# print(str1)
# str = "   youko ngge***  "
# str1 = str.strip("* ")
# print(str1)

import string
import math
# from string import make
# table = maketrans('cs','kz')

# print(help(string))
# print(dir(math))

# print(string.__doc__)


# s = (x for x in range(1,11))
# print(list(s))

def f(x):
    return x*x

# lists = [1,2,3,4,5,6,7]
# result = map(f,lists)
# print(list(result))
from functools import reduce

#
# def f(x,y):
#     return x+y
#
# lists = [1,2,3,4,5]
# result = reduce(f,lists)
# print(result)
# L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
# print(sorted(L))

print(type(123))