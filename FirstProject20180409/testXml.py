#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/4/16 15:35
# @author :shangxudong
# @File   : testXml.py
# @Software: PyCharm Community Edition


import xml.etree.ElementTree as ET

# 解析xml文件得到树
tree = ET.parse("result.xml")
# 获取根节点
root = tree.getroot()

# print(root.tag)
# print(root.attrib)

# for child in root:
#     for subchild in child:
#         print(subchild.tag)
#         print(subchild[0][1].text)

for neighbor in root.iter("key"):
    key = neighbor.text
    print(neighbor.tag, ":",key)

