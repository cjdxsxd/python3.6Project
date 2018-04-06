#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @time 2018/3/17 17:53
# @autor:shangxudong
# @name: get_LoggerDemo.py
# @software: PyCharm
import logging
import os

#初始化log对象
logger = logging.getLogger("日志模块名称")
#设置log级别，NOTSET < DEBUG < INFO < WARNING < ERROR < CRITICAL这几种级别，日志会记录设置级别以上的日志
logger.setLevel(logging.DEBUG)
#handler分两种：streamHandler（输出到控制台）和fileHandler（输出到文件）
file_name = os.path.join(os.getcwd(),'filelog.log')
fh = logging.FileHandler(filename=file_name,encoding='UTF-8')
fh.setLevel(logging.DEBUG)
sh = logging.StreamHandler()
sh.setLevel(logging.DEBUG)
#设置日志格式
formatter = logging.Formatter("%(asctime)s-%(name)s-%(levelname)s-%(message)s")
fh.setFormatter(formatter)
sh.setFormatter(formatter)
#将相应的handler添加到log对象
logger.addHandler(fh)
logger.addHandler(sh)
#开始打印日志
logger.debug("debug信息")
logger.info("info信息")
logger.warning("waring信息")
logger.error("error信息")
