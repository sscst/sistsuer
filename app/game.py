#!/usr/bin/env python  
# -*- coding: utf-8 -*- 

#0 for insert ; 1 for get ; 2 for update
def user_status(uid,type,g,**kw):
    if type == 0 :
        g.cur.execute("INSERT INTO story VALUES('%s','%s','%s','%s')" %(uid,'g0','N','code'))
    elif type == 1 :
        g.cur.execute("SELECT status FROM story WHERE uid = '%s'" % uid)
        result = g.cur.fetchall()
        if not result :
            return "new"
        return result[0][0]
    else :
        g.cur.execute("UPDATE story SET status = '%s' WHERE uid = '%s'" %(kw["status"],uid))
    g.conn.commit()
    return "ok"

def start(uid,text,g):
    user_status(uid,0,g)
    return "一场惊心动魄、谜团重重的冒险即将展开，让我们共同探寻「逸仙传说」的秘密。\n\n本游戏谨献给我们的信科女生们，祝她们女生节快乐！\n\n回复“开始游戏”展开信科女神冒险之旅"

def g0(uid,text,g):
    if text == "开始游戏":
        user_status(uid,2,g,status="g1")
        return "在中山大学，流传着许许多多不为人知的谜题，甚至，没有人知道答案。\n\n为什么校训中的“眀辨”用的是古体“眀”字？\n为什么中山大学东校区的网络一直异常？\n为什么每一个校区都有孙中山的铜像？\n\n但是那么多的传说，都不及那个「逸仙传说」更加惊心动魄。因为，那是真的。\n\n我叫辛珂，是一名信科院的普通女生，平时过着打打代码、泡泡图书馆的生活。但这普通的生活却被那一个奇幻的夜晚所打破。让我来慢慢告诉你们…\n\n回复“倾听” 分享信科女神的故事。\n回复“yy” yy让信科女神铭记的那一夜"
    return "except"

def g1(uid,text,g):
    if text == "倾听":
        user_status(uid,2,g,status="g2")
        return "那是一个普通的夜晚，我像平时一样，在新活的角落里坐着，看着晦涩难懂的证明。看了许久，甚是恼心，便下楼到中心花坛散心。\n\n夜阑人静，月华初上，中心花坛显得格外清幽。我闭着眼睛，感受这宁静。\n\n突然，一下响亮的提示音打断了这静谧。我掏出手机一看，是一条短信。\n\n“你想知道「逸仙传说」么？”\n\n回复“想”了解传说\n回复“不想”继续散心"
    elif text == "yy":
        return "某信科宅男：那一夜！？我的女神...\n\n信科女神：呵呵..."
    return "except"

def g2(uid,text,g):
    if text == "不想" :
        return "虽然这很有可能是一条无聊短信，但我仿佛觉得有种神秘的力量指引我去回复它。"
    elif text == "想":
        user_status(uid,2,g,status="g3")
        return "我下意识地看了看发件人的名字,竟只是一串乱码。应该是恶作剧吧，我想。但鬼使神差地，我回了一条“想”。\n\n几乎在瞬间，我收到了回复：\n\n「逸仙传说」\n 有秘闻称，孙逸仙先生早年在东洋发现了一样神器，传说得到神器后，将会发生一些不可思议的事情！\n\n可不知为何，孙先生将这块神器交给了日本好友梅屋庄吉先生保管。梅屋庄吉先生一直保管着这个物件，从未示人。\n\n而在孙逸仙先生逝世后，这位梅屋庄吉先生却突然花了大量的资金铸造了四尊孙中山铜像运送回国。\n\n表面上看，这是为了弘扬孙先生的主义，但年轻人，你相信这个说法么…\n\n回复“相信” 无条件接受弘扬主义的说法\n回复“不相信” 质疑这个说法"
    return "except"

def g3(uid,text,g):
    if text == "相信":
        return "喂喂喂，拜托，我的设定可是信科女神耶！敢不敢更土一点呀！"
    elif text =="不相信":
        user_status(uid,2,g,status="g4")
        return "就在我回复了神秘短信思绪万千的时候，短信提示音再次响起……\n\n年轻人\n你想探索真相么？\n那就追随真相的脚步\n用你的智慧解开这个神秘的「逸仙传说」\n大胆地告诉我:\n\nWhat do Atbash Chiper say to sroovh？\n\n你信科女神般的直觉感觉到，这是一个密码。\n\n回复答案（小写字母）解开谜题\n\nHINTS:你可以宣誓“我是信科女神”获得提示"
    return "except"

def g4(uid,text,g):
    if text == "我是信科女神":
        return "为什么不百度一下 Atbash Chiper （埃特巴什码）？"
    elif text == "hilles":
        user_status(uid,2,g,status="g5")
        return "手机荧幕的光闪烁着，仿佛在试探我的反应。\n\n“Hilles”我不由得读出了声。突然，我仿佛明白了！\nHilles！\n喜乐斯！\n\n“中山大学东校区图书馆五楼是喜乐斯藏书室，喜乐斯藏书来自哈佛大学哈佛学院图书馆下辖的喜乐斯图书馆，由哈佛大学无偿地捐赠给中山大学，建立两校间亲密无间的兄弟情谊。”\n\n那段大一开学时接受的图书馆历史教学材料，又闪现在脑海里！\n难道，「逸仙传说」的秘密就在喜乐斯藏书室么？\n\n回复“喜乐斯”前往喜乐斯藏书室"
    return "作者：哎，女神好像觉得这不是正解耶，再想想？"

def g5(uid,text,g):
    if text == "喜乐斯":
        user_status(uid,2,g,status="gs1")
        return "http://sysugril-sscst.dotcloud.com/static/img/hilles_pic.png#e#到了喜乐斯藏书室，环视四周，好像没有任何可疑的线索。突然，我有一种直觉。喜乐斯揭牌的板有可能有密码。\n我上前去，仔细观察。发现被红布遮着的地方，有一些奇怪的符号。\n\n回复“查看” 研究奇怪符号"
    return "except"

def gs1(uid,text,g):
    if text == "查看":
        user_status(uid,2,g,status="g6")
        return "http://sysugril-sscst.dotcloud.com/static/img/hilles_code.png#e#我想，这些图案总觉得有些规律，可能与某些数字有关...\n\n回复答案（一行阿拉伯数字）解开密码\n\nHINTS:你可以宣誓“我是信科女神”获得提示"
    return "except"
        

def g6(uid,text,g):
    if text == "我是信科女神":
        return "这，不就是阿拉伯数字的轴对称加密么？"
    elif text == "35051989":
        user_status(uid,2,g,status="g7")
        return "35051989！？书刊号！我突然反应过来数字的含义。\n\n我立刻将校园卡押在图书馆助理那里，进入喜乐斯藏书室搜寻这本书。\n\n“3505…1989…找到了！《MINDFIELD（思想场）》！”我激动地把书从架子上取了下来，按捺住心中的兴奋，但它似乎没什么特别的，只是一部诗集而已。\n\n翻开绿色的封面，忽然，一张泛黄的纸片从书中掉落。我捡了起来，发现上面有字。\n\n浪清无点水,\n只因双目依。\n却把贞石綴，\n寻得逸仙回。\n\n我不由得发出惊叹，“这是一个新的线索！”信科女神敏锐的直觉告诉我，这小诗的前两句是字谜！\n\n回复答案解谜（两字）\n\nHINTS:你可以宣誓“我是信科女神”获得提示"
    return "作者：哎，女神好像觉得这不是正解耶，再想想？"

def g7(uid,text,g):
    if text == "我是信科女神":
        return "我私心想着，浪清两字没有一点一水，双目依在上面，这两个字，应该是……."
    elif text == "眼睛":
        user_status(uid,2,g,status="g8")
        return "我寻思着，“浪清无点水，只因双目依”不就是“眼睛”二字么！“却把贞石綴，寻得逸仙回”，也就是说，「逸仙传说」的线索在一块点缀着眼睛的普通石头上？\n\n中大怎么会有一块有眼睛的石头呢？\n\n我嗤笑着，想着可能是「逸仙传说」无解吧。从图书馆踱出来，看着谷河，才发现自己上大学那么久，都没有在中大悠闲地逛过这条河畔路。\n\n回复“谷河北路”在谷河北路散心\n回复“谷河南路”在谷河南路散心\n回复“君城”在君城湖畔餐厅吃东西"
    return "作者：哎，女神好像觉得这不是正解耶，再想想？"

def g8(uid,text,g):
    if text == "谷河南路":
        return "听同学说，南实验楼草丛有蛇！这个时候如果有高帅富陪就好了..但现在嘛，还是别走的好。（作者：广大SISTers们是不是心动了？）"
    elif text == "君城":
        return "虽然君城还有一些残羹剩饭，但是为了“要么瘦，要么死”计划，\n\n不！能！吃！东！西！\n\n所以还是去散心吧~"
    elif text =="谷河北路":
        user_status(uid,2,g,status="g9")
        return "沿着谷河散步，才发现中大有这么舒服的地方。\n\n晚风习习地拂过脸颊，路灯点点映在河面上。氤氲躺在天边，恬静之间又有几分庄严。\n\n阳光的余温还没消散，我就这么漫无目的沿着谷河北路一直走着，脑海里还在纠结着那个荒谬的「逸仙传说」，自己也不禁觉得好笑。\n\n“一块有眼睛的石头，怎么会有这种东西呢？”我自嘲道。正说着，突然间那块政务学院门前的校训石映入了眼帘。\n“这块石头！？不就是…”我一时间被震惊得说不出话。\n\n回复令女神震惊的原因（一个字）\n\nHINTS:你可以宣誓“我是信科女神”获得提示"
    return "except"

def g9(uid,text,g):
    if text =="明" or text == "眀":
        user_status(uid,2,g,status="g10")
        return "http://sysugril-sscst.dotcloud.com/static/img/stone_front.png#e#我猛地发现，校训中那个被沿用的错别字“眀”，不就正好让石头上多了眼睛么！这就是那块有眼睛的石头啊！\n\n我快步上前，仔细端详这块校训石。\n\n石头有正面和背面两面，而校训石底座右下角上有“赠于2009.11.12日 中山大学海外学生会敬赠”的字样。\n\n回复“正面”搜寻校训石正面\n回复“背面”去石头背面观察\n回复“底座”仔细分析石头底座"
    elif text == "我是信科女神":
        return "校训石上有校训，但校训中含有一个无法让人解释的细节让石头带上眼睛。同时，这也是中山大学许多没有解释的传闻之一。"
    return "作者：这可不是让女神震惊的字啊，你能懂女神的心嘛？"

def g10(uid,text,g):
    if text == "正面":
        return "我来到这块校训石旁，两米高的巨石在夜幕下更显威严。路灯的白光洒上面，映得千年不变绿底校训更加苍劲。\n\n看着那熟悉而又陌生的校训，我陷入沉思。博学，审问，慎思，眀辨，笃行。这道理简单，说的是广泛学习，仔细探究，谨慎思考，明辨是非，切实施行。\n\n可能那个“眀”字，除了隐藏逸仙传说以外，还希望中大的学子用眼去明辨是非，不能道听途说吧。\n\n2009年11月12日？中山大学海外学生会？那是一个什么样的日子？为什么海外学生会赠送这块石头呢？\n\n但我一点头绪都没有，要不再找找吧。"
    elif text == "底座":
        return "http://sysugril-sscst.dotcloud.com/static/img/stone_bottom.png#e#2009年11月12日？中山大学海外学生会？那是一个什么样的日子？为什么海外学生会赠送这块石头呢？\n\n2009年11月12日我默记下这个日子，拿出手机，google一下！在一大堆冗杂繁复的信息中，我看到了一条让我眼前一亮的信息。\n\n2009年11月12日，中山大学在东校区图书馆广场隆重举行了迎校庆85周年升旗仪式。\n\n那一天是校庆85周年！但当时大学城已经建成好几年了，为什么中山大学海外学生会不挑80周年赠送校训石,而挑85周年呢?\n\n80周年可是大庆，为什么不在这个年份送呢？\n\n这好像有些什么关联，但是我抓不到。"
    elif text == "背面":
        user_status(uid,2,g,status="g11")
        return "http://sysugril-sscst.dotcloud.com/static/img/stone_back.png#e#我想，秘密应该藏在校训石的背面。于是，走了过去仔细观察。发现石头后面更多的信息，有赞助校训铭校友芳名，还有一篇校训石铭文。\n\n这么多字，其中肯定有秘密！我痴痴地想，但现在时候也不早了，要快点回宿舍了。\n\n回复“读铭文”阅读校训石铭文\n回复“芳名录”研究赞助校训铭校友的芳名录\n回复“离开”离开默园的校训石回宿舍休息"
    return "except"

def g11(uid,text,g):
    if text == "读铭文":
        return "http://sysugril-sscst.dotcloud.com/static/img/stone_poem.png#e#我仔细阅读陈永正老先生大气磅礴的校训石铭文“天下为公，大哉逸仙!......”\n\n我深深地被苍劲有力的书法折服，对于这段铭文，虽不明，但觉厉！这肯定与「逸仙传说」的真相有关。\n\n于是，我立刻把这铭文摘抄到小本子里。"
    elif text == "芳名录":
        g.cur.execute("UPDATE story SET name_status = 'Y' WHERE uid = '%s'" % uid )
        g.conn.commit()
        return "http://sysugril-sscst.dotcloud.com/static/img/stone_list.png#e#我暗自忖思，这个芳名录…好长！\n\n数了一下，12列12行，有3个两个字名字。\n\n仔细一看，什么名字都有。感觉上，这些名字里没什么特别大的秘密。\n\n但信科女神的缜密告诉我，不能漏下任何一个细节，我决定把这名单抄下来！\n\n得到笔记【芳名录】\n\n我看了看时间，已经够晚了..."
    elif text == "离开":
        g.cur.execute("SELECT name_status FROM story WHERE uid = '%s'" % uid)
        result = g.cur.fetchall()
        if result[0][0] == 'Y':
            user_status(uid,2,g,status="g12")
            return "实在是太累了，而晚上的中大默园，仿佛有种诡异的气氛，我实在没有情绪再对着这块石头研究了，决定回宿舍休息。\n\n我拖着疲惫的身体回到宿舍，休息了一会，又开始思索今天的奇遇。\n\n宿舍里一片和谐，对面床的小奇在追韩剧，而旁边的小竹在跟男朋友视频聊天，学霸小璇正在和小骄讨论题目。似乎没有人注意到我今天的一切。\n\n我轻笑了一下，可能我有些走火入魔了吧？决定不再理会「逸仙传说」，上网放松一下。打开电脑，准备刷刷微博。\n\n就在这时，突然断网了！\n\n“怎么又断网了！不是今天网络中心说修好了么！”宿舍的人十分不满。\n\n而就在这个集体断网的时候，看着我的电脑屏幕，我傻掉了。这个不是一般的蓝屏死机错误，这个是…\n\n回复“抱怨”抱怨中大断网\n回复“解读”解读蓝屏信息\n回复“安抚”安抚受伤室友"
        else :
            return "总觉得校训石背面还有一些信息我没注意，不如过去看看？"
    return "except"

def g12(uid,text,g):
    if text == "抱怨":
        return "你#￥@&*……的中大**网络！你说你那**网络怎么这么**！\n\n（编导：喂！你是女神啊，注意设定啊！）"
    elif text == "安抚":
        return "读者：安抚你妹啊！不要拖延剧情！"
    elif text == "解读":
        user_status(uid,2,g,status="g13")
        return "http://sysugril-sscst.dotcloud.com/static/img/screen.png#e#虽然对网络很失望，但是想解开「逸仙传说」的斗志重新激起！\n\n观察那一堆数字，感觉十分凌乱。\n\n但好像对这些数据好熟悉。\n\n回复“数电”觉得在数字电路课上见过\n回复“军理”想应该是军事理论课上见过\n回复“思考”再思考一下什么地方觉得熟悉"
    
    return "except"

def g13(uid,text,g):
    if text == "数电" :
        return "你以为这是做数电题么！这个故事没有卡诺图化简！"
    elif text == "军理":
        return "女神温馨提示：请不要上升到军事机密，这就是一个小小的「逸仙传说」哦亲~"
    elif text == "思考":
        user_status(uid,2,g,status="g14")
        return "我仔细观察矩阵，发现都是1、0和x，排列似乎也没什么规律。\n\n“这有12行…有12列…有3个叉叉…有2个一。”我自言自语道。\n\n咦，等等…这些数据好像很熟悉…\n\n回复“使用物品”查看笔记本"
    return "except"

def g14(uid,text,g):
    if text == "使用物品":
        user_status(uid,2,g,status="g15")
        return "http://sysugril-sscst.dotcloud.com/static/img/list_code.png#e#这个也是12行12列还有3个空白处！\n\n难道，这其中有什么奥秘么？\n\n如果把这两个对应起来的话，那么…\n\n回复答案（两字）\n\nHINTS:你可以宣誓“我是信科女神”获得提示"
    return "except"

def g15(uid,text,g):
    if text == "我是信科女神":
        return "我记得，矩阵里面1代表的是正确，0代表的是错误，X代表的是任意值。那如果1代表正确的话，对应回芳名录的话…"
    elif text == "瀛友" or text == "友瀛" :
        user_status(uid,2,g,status="g16")
        return "分离出来，两个字就是“瀛友”。“瀛”字当然指的就是日本，而“友”就是朋友的意思。那么，下一个地点，应该跟一个日本友人关系密切！\n\n突然想起，短信里的「逸仙传说」不就提到了一个日本友人么！？难道是他?\n\n“梅屋庄吉先生却突然花了大量的资金铸造了四尊孙中山铜像运送回国。”\n\n难道说，秘密就隐藏在孙逸仙的铜像中么！\n\n回复“铜像”前往孙逸仙铜像探索秘密"

def g16(uid,text,g):
    if text == "铜像":
        user_status(uid,2,g,status="g17")
        return "我激动地冲去冲往逸仙大道，到那座庄严的孙先生铜像前。我瞻仰着孙先生的铜像，饱含敬畏之心。「逸仙传说」的秘密，难道就在这里么？\n\n孙先生铜像英伟地屹立在东校区逸仙大道的中轴线上，面对牌坊，眺望远方，仿佛守护着这所凝聚伟人心血的中山大学。\n\n回复“底座”搜索大理石底座？\n回复“铜像”搜索孙中山铜像？"
    return "except"

def g17(uid,text,g):
    if text == "底座":
        return "我仔细搜索，看到孙逸仙铜像后的话。\n\n“本校孙中山铜像原为先生故友日人梅屋庄吉所赠。一九三三年冬奉置于我校石牌旧址，后院系调整，遂于一九五六年冬迎置于康乐园。二〇〇四年秋，东校区落成。蒙马万祺先生捐款复制原样。今事竣，乃延置于此。”\n\n看来，铜像确实与日本友人有关系！但是这里除了这篇铭文，什么都没有。"
    elif text == "铜像":
        user_status(uid,2,g,status="finish")
        return "http://sysugril-sscst.dotcloud.com/static/img/mrsun.png#e#我走近观察，铜像左手叉腰，右手如同抽筋一般地直立着，左脚踩住铜像底座，神情显得严肃。\n\n我突然想起人的姿势是具有含义的！\n\n仔细观察，我发现，孙先生的右手的手势叫做竖手掌叫停，意在警告前面的人不要上前。而他的左脚微微前倾踩住木板，显示出他的心虚，可能在隐瞒什么！\n\n铜像本身，有问题！\n\n我跳起来，用手敲了一下铜像。\n\n“哐！”是空心的！\n\n于是，我费尽力，爬了上铜像的底座，突然发现，孙先生左脚踩着的底座下面，好像有些什么东西。\n\n回复“取出”取出铜像底座的物品"
    return "except"

def finish(uid,text,g):
    if text == "取出":
        g.cur.execute("DELETE FROM story WHERE uid='%s'" % uid)
        g.conn.commit()
        return "是一块铜片！\n\n我拿出来仔细观察，发现精致的铜片上，有字！\n......\n(Legend of SYSU to be continued...)\n\n恭喜您完成了「逸仙传说」女生节游戏，虽然还未揭开「逸仙传说」的秘密，但信科女神很开心，她给你准备了一份丰厚奖品哦！\n\n凭此微信，您可以于2013年3月9日中午到三饭小广场前领取信科女神的礼物哦！\n\n本游戏谨献给我们的信科女生们，祝她们女生节快乐!：）\n\n特别鸣谢：\n竹子\n骄妹\n小蛙"
    return "except"

status_dic = {
    "new":start,
    "g0":g0,
    "g1":g1,
    "g2":g2,
    "g3":g3,
    "g4":g4,
    "g5":g5,
    "gs1":gs1,
    "g6":g6,
    "g7":g7,
    "g8":g8,
    "g9":g9,
    "g10":g10,
    "g11":g11,
    "g12":g12,
    "g13":g13,
    "g14":g14,
    "g15":g15,
    "g16":g16,
    "g17":g17,
    "finish":finish
}


def game(uid,text,g):
    if text == '离开游戏':
        g.cur.execute("DELETE FROM story WHERE uid = '%s'" % uid)
        g.conn.commit()
        return "信科女神还是很希望解出「逸仙传说」的秘密\n下次一定要与女神走到最后喔！\n\n回复“女神冒险”就可以重新开始游戏\n\n除了聊天，您还可以发送#加任何希望信科学生会为您做的到本微信，我们将会及时回复。同时，十分欢迎您能对信科学生会的工作提出质疑与建议，让我们能为信科学子提供更好的服务。\n\n你的希望，我的可能!\n\n信息科学与技术学院学生会"
    elif text == "重新开始":
        user_status(uid,2,g,status="g1")
        msg = "在中山大学，流传着许许多多不为人知的谜题，甚至，没有人知道答案。\n\n为什么校训中的“眀辨”用的是古体“眀”字？\n为什么中山大学东校区的网络一直异常？\n为什么每一个校区都有孙中山的铜像？\n\n但是那么多的传说，都不及那个「逸仙传说」更加惊心动魄。因为，那是真的。\n\n我叫辛珂，是一名信科院的普通女生，平时过着打打代码、泡泡图书馆的生活。但这普通的生活却被那一个奇幻的夜晚所打破。让我来慢慢告诉你们…\n\n回复“倾听” 分享信科女神的故事。\n回复“yy” yy让信科女神铭记的那一夜"
        g.cur.execute("UPDATE story SET past_content = '%s',name_status ='N' WHERE uid='%s'" %(msg,uid))
        g.conn.commit()
        return msg
    elif text == "重发信息":
        g.cur.execute("SELECT past_content FROM story WHERE uid = '%s'" % uid)
        result = g.cur.fetchall()
        return result[0][0]
    status = user_status(uid,1,g)
    msg = status_dic[status](uid,text,g)
    if msg == "except" :
        return "信科女神提醒：你说了啥？请按照我们的选项进行哦！\n\n回复“重新开始”从头开始玩游戏\n回复“重发消息”应对无回复的指令\n回复“离开游戏”离开游戏"
    g.cur.execute("UPDATE story SET past_content = '%s' WHERE uid='%s'" %(msg,uid))
    g.conn.commit()
    return msg




