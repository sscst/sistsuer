#!/usr/bin/env python  
# -*- coding: utf-8 -*- 
from flask import url_for, Flask,render_template,request,session,redirect,Response,g
import sys,time
from xml.dom import minidom
import MySQLdb,json
from get_response import *
from const import *
from gmail import *
from game import game,user_status

reload(sys)
sys.setdefaultencoding('utf-8')

app = Flask(__name__)
app.config.from_pyfile('config.cfg')

def message(xml):
    dom = minidom.parseString(xml)
    root = dom.firstChild 
    children = [node for node in root.childNodes if node.nodeType == 1]

    mes_type = children[3].childNodes[0].data
    uid = children[1].childNodes[0].data
    me = children[0].childNodes[0].data
    status = user_status(uid,1,g)

    mes = "想跟我聊天?直接输入文字就好了"
    
    if mes_type == 'text':
        text = children[4].childNodes[0].data
        if text == 'Hello2BizUser':
            mes = "欢迎您关注中大信科学生会的微信！\n\n您可以通过#加吐嘈内容向我们提任何意见，我们将会及时回复。十分欢迎您对信科学生会的工作提出质疑与建议。此外，您可以输入任何文字跟我聊天,打发闲暇时间。\n\n信科女生节「逸仙传说」微信游戏正式上线！一个信科女神的奇幻故事，一段尘封许久的逸仙传说，一次精彩绝伦的冒险之旅！回复“女神冒险”开始一次伟大的冒险旅程！\n\n你的希望，我的可能！\nYour will, we will!"
        elif text[0] == '#':
            mes = advise(text[1:])
        elif text == '女神冒险' or not status == 'new' :
            mes = game(uid,text,g)
        else :
            mes = get_response(text)

    word_list = mes.split('#e#')
    if len(word_list) == 2 :
        return replypic % (uid,me,'%d' % (int(time.time())),word_list[1],word_list[0],word_list[0])
    return replytext % (uid,me,'%d' % (int(time.time())),word_list[0])

def reply(result):
    return replytext % result

def advise(str_text):
    g.cur.execute("INSERT INTO advise VALUES('%s')" % str_text)
    g.conn.commit()
    return "同学，你的建议我们已经收到啦，谢谢你对信科学生会的支持！"


@app.after_request
def get_close(response):
    g.cur.close()
    g.conn.close()
    return response

@app.before_request
def connect_db():
    with open("/home/dotcloud/environment.json") as f :
        evn = json.loads(f.read())
    g.conn =  MySQLdb.Connection(host=evn["DOTCLOUD_DB_MYSQL_HOST"], 
                                 user=evn["DOTCLOUD_DB_MYSQL_LOGIN"], 
                                 passwd=evn["DOTCLOUD_DB_MYSQL_PASSWORD"], 
                                 db='sysu',
                                 port=int(evn["DOTCLOUD_DB_MYSQL_PORT"]),
                                 charset='utf8')
    g.cur = g.conn.cursor()

@app.route("/",methods=['GET','POST'])
def index():
    if request.method == 'POST':
        xml = request.data
        if not xml :
            xml = request.form.keys()[0]
        return message(xml)
    return "这里是中大信科的微信平台后台哦"

@app.route("/pic")
def pic():
    return render_template('pic.html')

@app.route("/mail",)
def mail():
    result = send_mail("470840005@qq.com","test","这里是云发送的哦")
    if result :
        return "成功！"
    return "失败"
   
if __name__ == "__main__":
    app.run()
