#!/usr/bin/env python
# _*_ coding: utf-8 _*_
# @Time   :2018/4/10 15:07
# @author :shangxudong
# @File   : runAll.py
# @Software: PyCharm Community Edition
import unittest
import test_001
from HTMLTestRunner import HTMLTestRunner
import time
import smtplib
from email.message import EmailMessage
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


# emsg = EmailMessage()
# emsg.set_content("接口报告")
# emsg['Subject']="接口报告"
# emsg['From']="3360048@163.com"
# emsg['To']="469820049@qq.com"
# # 发送附件
filename = "./testResult/"+"17-56-22 2018-04-10_result.html"
#
multi = MIMEMultipart()
# 添加html附件
att1 = MIMEText(open(filename, 'rb').read(), 'base64', 'utf-8')
att1['Content-Type'] = "'application/octet-stream"
att1['Content-Disposition'] = 'attachment; filename="result.html"'
multi.attach(att1)

# 添加照片附件
filename2 = './testFile/'+"sxd1.jpg"
img = MIMEImage(open(filename2,'rb').read())
img['Content-Disposition'] = 'attachment; filename="sxd.jpg"'
multi.attach(img)

multi['Subject'] = "接口报告"
multi['From'] = "3360048@163.com"
multi['To'] = "469820049@qq.com"
content = '这是一封测试邮件，用于测试MIMIMultipart，并且添加html附件，以及邮件内容'
# 添加邮件正文
multi.attach(MIMEText(content,_subtype='plain',_charset='utf-8'))

sm = smtplib.SMTP()
sm.connect("smtp.163.com")
sm.login("3360048@163.com","421127Cjdxsxd")
sm.send_message(multi)

# 自动发现用例
test_dir = "./testCase"
discover = unittest.defaultTestLoader.discover(test_dir,pattern="test*.py")

if __name__ == '__main__':
    # suit = unittest.TestSuite()
    # suit.addTest("test_001.test_getNoParams")

    now = time.strftime('%H-%M-%S %Y-%m-%d')
    print(now)
    filename = './testResult/'+now+"_result.html"
    print(filename)
    with open(filename, 'wb') as fp:
          # runner = unittest.TextTestRunner()
        runner = HTMLTestRunner(stream=fp, title="接口测试",description="测试接口1")
        runner.run(discover)
