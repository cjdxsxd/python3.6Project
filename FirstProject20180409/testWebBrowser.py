#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/4/13 16:46
# @author :shangxudong
# @File   : testWebBrowser.py
# @Software: PyCharm Community Edition
import webbrowser
from webbrowser import Chrome
import cgitb
import cgi


cgitb.enable(display=0,logdir="D:\\cgilog.log")

url = 'http://www.baidu.com/'
# webbrowser.open(url)

# webbrowser.open_new(url)
# webbrowser.open_new_tab(url)

# r = webbrowser.get()

# print(r)

chromepath = r'C:\Program Files (x86)\Google\Chrome\Application'
# webbrowser.register('chrome',Chrome('chrome'))
# webbrowser.get(using='chrome').open(url,new=2,autoraise=True)

# print(r2)

# webbrowser.get(using='chrome').open(url)

form = cgi.FieldStorage()
if "name" not in form or "addr" not in form:
    print("<H1>Error</H1>")
    print("please fill in the name and addr fields.")

# print("<p>name:",form["name"].value)
# print("<p> addr :",form["addr"].value)

