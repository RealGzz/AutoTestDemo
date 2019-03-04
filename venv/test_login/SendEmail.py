#coding:utf-8

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_mail(sender, psw, receiver, smtpserver,reportfile, port=465):
    '''发送最新的测试报告内容'''
    #打开测试报告
    with open(reportfile, "rb") as f:
        mail_body = f.read()
    # 定义邮件内容
    msg = MIMEMultipart()
    body = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = u"自动化测试报告"
    msg["from"] = sender
    msg["to"] = ','.join(receiver)#.join的用法。。。。
    msg.attach(body)
    # 添加附件
    att = MIMEText(open(reportfile, "rb").read(), "base64", "utf-8")
    att["Content-Type"] = "application/octet-stream"
    att["Content-Disposition"] = 'attachment; filename= "report.html"'
    msg.attach(att)
    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
    except:
        smtp = smtplib.SMTP()
        smtp.connect(smtpserver,port)
    # 用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    reportfile = u"/Users/ghx/PycharmProjects/firefoxDemo/venv/test_login/TestReportSir.html"#测试报告路径
    smtpserver = "smtp.qq.com"  #  邮箱服务器
    sender = "1679466787@qq.com" # 自己的账号
    psw = "txrpvxjmnjrmdecj" #自己的授权码
    receiver = ['gengzhuang@lovinc.com','fun_gz@126.com'] #对方的账号
    send_mail(sender, psw, receiver, smtpserver,reportfile)