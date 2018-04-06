#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @time 2018/3/21 21:19
# @autor:shangxudong
# @name: test_saxParserXmlDemo.py
# @software: PyCharm
from xml.sax import parse
from xml.sax import ContentHandler


class SaxParserContentHandler(ContentHandler):
    def __init__(self):
        """只想取xml2个字段内容"""
        self.currentData = ""
        self.type = ""
        self.typename = ""

    def startElement(self, name, attrs):
        self.currentData = name
        if name == "movie":
            print("movie:")

    def characters(self, content):
        if self.currentData == "type11":
            self.type = content
        if self.currentData == "typename":
            self.typename = content

    def endElement(self, name):
        if self.currentData == "type11":
            print("Type11:", self.type)
        if self.currentData == "typename":
            print("typeName:", self.typename)
        self.currentData = ""


if '__name__' == '__main__':

    handler = SaxParserContentHandler()
    parse("testData.xml", handler)
