#发送邮件公共文件

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header
import os

#==============定义发送邮件 ===============

def send_mail(file_new):
    f = open(file_new,'rb')
    #读取测试报告正文
    mail_body = f.read()
    f.close()
    # 发送邮箱服务器
    smtpserver = "smtp.qq.com"
    # 发件人邮箱
    sender = '10196822@qq.com'
    # 接收人邮箱
    receiver = 'weilin@citicguoanbn.com'
    # 发送邮箱用户信息
    username = '10196822@qq.com'
    # 客户端授权码
    password = 'ebazzhbxyxbqbjef'

    #通过  模块构造的带附件的邮件如图
    msg = MIMEMultipart()
    #编写html类型的邮件正文，MIMEtext()用于定义邮件正文
    #发送正文

    text = MIMEText(mail_body, 'html', 'utf-8')
    text['Subject'] = Header('自动化测试报告', 'utf-8')
    msg.attach(text)
    #发送附件
    #Header()用于定义邮件标题
    msg['Subject'] = Header('XXXX自动化测试报告', 'utf-8') #具体的项目需要具体化
    msg_file = MIMEText(mail_body, 'html', 'utf-8')
    msg_file['Content-Type'] = 'application/octet-stream'
    msg_file["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_file)

# 如果只发正文的话，上面的代码 从password 下面到这段注释上面
# 全部替换为下面的两行代码即可，上面的代码是增加了发送附件的功能。
#     text = MIMEText(mail_body, 'html', 'utf-8')
#     text['Subject'] = Header('自动化测试报告', 'utf-8')


    #一样的逻辑，不一样的写法导致上面的发送失败，下面这种发送成功，所以要使用msg['from']这种写法
    msg['from'] = '10196822@qq.com'  # 发送邮件的人
    msg['to'] = 'weilin@citicguoanbn.com'
    # smtp = smtplib.SMTP('smtp.163.com', 25)  # 连接服务器
    smtp = smtplib.SMTP()
    smtp.connect('smtp.qq.com')
    smtp.login(username, password)  # 登录的用户名和密码
    smtp.sendmail(msg['from'], msg['to'], msg.as_string())  # 发送邮件
    smtp.quit()
    print('sendmail success')

#======================查找最新的测试报告==========================

def new_report(testreport):
    #方式1：
    # lists = os.listdir(testreport)
    # lists.sort(key = lambda fn: os.path.getmtime(testreport + '\\' + fn))
    # file_new = os.path.join(testreport,lists[-1])
    # print(file_new)
    # return file_new

    #方式2：
    dirs = os.listdir(testreport)
    dirs.sort()
    newreportname = dirs[-1]
    print('The new report name: {0}'.format(newreportname))
    file_new = os.path.join(testreport, newreportname)
    return file_new
