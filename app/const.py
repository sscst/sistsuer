#!/usr/bin/env python  
# -*- coding: utf-8 -*- 


replytext = '''<xml> 
	        <ToUserName><![CDATA[%s]]></ToUserName> 
	        <FromUserName><![CDATA[%s]]></FromUserName>  
		<CreateTime>%s</CreateTime>  
		<MsgType><![CDATA[text]]></MsgType>  
		<Content><![CDATA[%s]]></Content>  
		<FuncFlag>0</FuncFlag>  
		</xml>'''

replypic = ''' <xml>
                 <ToUserName><![CDATA[%s]]></ToUserName>
                 <FromUserName><![CDATA[%s]]></FromUserName>
                 <CreateTime>%s</CreateTime>
                 <MsgType><![CDATA[news]]></MsgType>
                 <ArticleCount>1</ArticleCount>
                    <Articles>
                       <item>
                       <Title><![CDATA[]]></Title> 
                       <Description><![CDATA[%s]]></Description>
                       <PicUrl><![CDATA[%s]]></PicUrl>
                       <Url><![CDATA[%s]]></Url>
                       </item>
                    </Articles>'''

reply=["这个问题我不大懂啊，你能教教我嘛？用‘问...答...’的句式哦",
       "这是哪来的新词？教教我好吗？‘问...答...’就可以了哦",
       "你是火星来的？教教我火星词吧！‘问...答...’我就能懂哦",
       "在那山的那边，海的那边...这话我听不懂，告诉我什么意思好吗？'问...答...'的方法告诉我哦"]
