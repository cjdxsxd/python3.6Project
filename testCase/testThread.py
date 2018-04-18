#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/4/18 18:12
# @author :shangxudong
# @File   : testThread.py
# @Software: PyCharm Community Edition
import threading

def test1(name):
    print(name+"hello")

def test2(a,b):
    sum = a+b
    print(sum)


t1 = threading.Thread(target=test1,name="测试线程1",args=("sxd",))
t2 = threading.Thread(target=test2,name="测试线程2",args=(2,3))
print(t1.getName())
t1.start()
print(t2.getName())
t2.start()

lock = threading.Lock()
lock.acquire()
try:
    t1.run()
finally:
    lock.release()

