#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/4/16 11:12
# @author :shangxudong
# @File   : testConfigParser.py
# @Software: PyCharm Community Edition

import configparser



cfg = configparser.ConfigParser()
# sec = cfg.sections()
# print(sec)
cfg.read("project_Config.ini")

cfg.sections()

dbconn = cfg['db_connect']

print(dbconn["name"])