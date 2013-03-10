# -*- coding: utf-8 -*-  
#!/usr/bin/env python

import smtplib
from email.mime.text import MIMEText
from email.Header import Header
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart
import smtplib, datetime

def send_mail(to_list,sub,content,file):
    mail_host="smtp.sina.com"
    mail_user="470840005qq"
    mail_pass="19920820"
    mail_postfix="sina.com"
    me=mail_user+"<"+mail_user+"@"+mail_postfix+">"

    ms=MIMEMultipart()
    ms['Subject'] = Header(sub,'utf-8')
    ms['From'] = me
    ms['To'] = to_list

    msg = MIMEText(content)
    msg.replace_header('Content-Transfer-Encoding', 'quoted-printable')

    file_mail = MIMEText(file.read(),'base64','utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = "attachment; filename='weibo.txt'"

    ms.attach(msg)
    ms.attach(file_mail)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)
        s.login(mail_user,mail_pass)
        s.sendmail(ms, to_list, msg.as_string())
        s.close()
        return True
    except Exception, e:
        return False

