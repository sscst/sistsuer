#!/usr/bin/env python  
# -*- coding: utf-8 -*- 
import urllib,urllib2,re
from xml.dom import minidom
import random
from const import reply

def get_response(text):
    addr = "\n\n发送“女神冒险”可以与信科女神一同解开「逸仙传说」的神秘面纱哦！\n\n你还可以发送‘#’后跟吐嘈内容给我们提意见！"
    p = "/:"
    r = re.findall(p,text)
    if r :
        return "禁止纯表情回复！！"
    url = "http://weixen.sinaapp.com/api2.php?" 
    parm1={
        "chat":text
    }
    c = urllib2.urlopen(url+urllib.urlencode(parm1))
    dom = minidom.parseString(c.read())
    root = dom.firstChild
    if not root.childNodes[0].childNodes or not root.childNodes[0].childNodes[0].data.find("抱歉，小九") == -1:
        return random.choice(reply) + addr
    elif root.childNodes[0].childNodes[0].data == '*':
        return random.choice(reply) + addr
    return root.childNodes[0].childNodes[0].data
    
