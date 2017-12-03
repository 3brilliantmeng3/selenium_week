
import os
import smtplib
import  unittest

# HTMLTestRunner 是基于unittest框架的一个扩展,该文件可从网上下载
import time
from email.header import Header
from email.mime.text import MIMEText

from lib.HTMLTestRunner import HTMLTestRunner


def send_mail(path):
    f = open(path,'rb')  # 使用二进制方式读取html文件的内容,作为邮件的正文
    mail_boby = f.read()   # 读取html文件的内容,作为邮件的正文
    file.close()

    # 要想发邮件,需要把二进制的内容转成MIME格式
    # MIME multipurse 多用途,Intenet互联网 mail邮件 Extension 扩展
    # 这种格式是对邮件协议的扩展,使邮件不仅支持文本格式,还支持多媒体多种格式,比如说图片,音频,二进制文件等
    msg = MIMEText(mail_boby,'html','utf-8')    # 把二进制转换成MIME文本格式
    # msg 是一种字典的类型,字典类似与数组,区别是:1/字典是无序的

    msg['subject'] = Header("自动化测试报告",'utf-8')   # 设置邮件的主题
    # 如果想用 客户端软件,或者自己写代码登陆邮箱,很多类型邮箱的服务器需要单独设置一个客户端授权码，为了邮箱安全着想

    #　发件箱统一用老师的
    msg['From'] = 'bwftest126@126.com'
    msg['To']='mengxia25@163.com'

    # 现在邮件内容已经准备好了,下面开始发生邮件
    # 发邮件手动步骤:
    # 1.打开登陆页面, 即链接邮箱服务器,才能够登陆邮箱
    # 要想链接服务器,首先必须清楚网络传输协议
    # http  ,https, ftp , socket,
    # 发邮件的协议一般有3种,要先清楚发邮件的邮箱支持哪种协议 POP3 SMTP IMAP
    # 我们要选一种传输协议,用来发邮件,smtp
    # simple mail transfer protocol 简单传输协议
    smtp = smtplib.SMTP()  # 实例化一个SMTP 类的对象
    smtp.connect("smtp.126.com")   # 链接126邮箱的服务器的地址 smtp.126.com

    # 2.登陆邮箱
    smtp.login('bwftest126@126.com','abc123asd654')
    # 3.发送邮件
    # 注意 msg是MIME
    smtp.sendmail( 'bwftest126@126.com', 'mengxia25@163.com', msg.as_string())


    # 4.退出邮件
    smtp.quit()
    print("mail has sent out!")









if __name__ == '__main__':
    # strftime() 通过这个方法了可以定义时间的格式
    now = time.strftime("%Y-%m-%d_%H-%M-%S")

    suite = unittest.defaultTestLoader.discover('./day5', '*Test.py')
    # 使用html 的测试用例运行器最终会生成一个html格式的测试报告
    # 我们是不是至少要指定测试报告的路径呢?
    base_path = os.path.dirname(__file__)
    path = base_path + "/report/report"+now+".html"
    file = open (path,'wb')
    HTMLTestRunner(stream=file ,title="海盗商城测试报告",description="测试环境:windows server 2008 +chrome").run(suite)
    file.close()
    # 我们要把html 作为邮件正文发送给相关干系人
    send_mail(path)
    # 这时生成的测试报告,只显示类名和方法名,只能给专业人员看
    # 应该将相关的手动测试用例的标题加到我们的测试报告
    # 我们自动化测试用例是从手工测试用例当中挑选出来的,手工测试用例怎么写,我们就怎么编写代码,所以我们的代码里可以体现手工测试用例的标题
    # 加一个时间戳,按照当前时间计算一个数字,把数字作为

