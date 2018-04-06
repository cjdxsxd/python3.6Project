#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @time 2018/3/17 20:02
# @autor:shangxudong
# @name: test_mySqlDemo.py
# @software: PyCharm
import pymysql
import ConfigData
from .import test_mySqlDemo
import test_mySqlDemo
import test_getDemo


import sys
print(sys.path)
#安装pymysql模块，导入模块
#创建连接
#创建游标cursor
#执行sql
#关闭游标
#关闭连接

conn = pymysql.connect(**ConfigData.sql_conn_dict)
cur = conn.cursor()

sql = "select * from sys_config"
cur.execute(sql)
data = cur.fetchone()
print (data)
cur.close()
conn.close()