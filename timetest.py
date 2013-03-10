#!/usr/bin/env python  
# -*- coding: utf-8 -*- 

import MySQLdb,time
from app.gmail import *


num = 1
while True :
    send_mail("470840005@qq.com","test%d" % num,'测试时间abc')
    num += 1
    time.sleep(60*5)
