#Creation Time: 2026.3.20
from pathlib import Path
import time
import sys
import pygame
import random

#============初始角色设置============

class Character:
    def __init__(self, name, full_name,age, hobbies, personality):
        self.name = name  #名字
        self.full_name = full_name  #完整名字
        self.age = age  #年龄
        self.hobbies = hobbies  #爱好
        self.personality = personality  #性格
        self.affection = 0  #初始好感度
        self.coolness = 0  #初始帅气值:)

    def affection_up(self, value):  #加好感度
        self.affection += value

    def affection_down(self, value):  #减好感度
        self.affection -= value

    def coolness_up(self, value):  #加帅气值
        self.coolness += value

    def coolness_down(self, value):  #减帅气值
        self.coolness -= value

#=============初始角色=============

character_protagonist = Character('None', 'None', 17, '无', '温柔、不善言辞')
character_1 = Character('千夏', '樱井千夏', 17, '写日记、吃甜食', '傲娇、温柔、不善言辞')

#=============初始音乐=============

pygame.mixer.init()
bgm_path = Path(__file__).parent / 'assets' / 'shichigatsunokomorebi.mp3'
pygame.mixer.music.load(str(bgm_path))
pygame.mixer.music.play(-1)

#=============定义函数=============

def talk(text, speed = 0.05):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(speed)

    print()

def choice(choices):
    for key, value in choices.items():
        talk(f'{key}:{value}')
    result = input('请选择：')
    time.sleep(0.5)
    return result

def date_setting(date, weather):
    time.sleep(1)
    print(f'{date}, {weather}')

#=============正式游戏=============

#游戏命名
talk('欢迎游玩！希望您能度过一段温柔、安静的游戏时光。请输入您的名字：')
character_protagonist.full_name = input()

talk('设定成功！\n'
    f'你好，{character_protagonist.full_name}！按enter键开始游戏。')
input()

#Part 1

date_setting('Mar.2, Monday', 'Rainy')

time.sleep(0.5)
text = ('清脆的闹钟声将你从睡梦中拽醒，手机上显示出时间：6时30分。拉开窗帘，灰蒙的天空不时落下几滴晶莹。\n'
        '是雨天呐...你小声嘟哝。但你的家离学校很近，只要跑得稍微快一点，就几乎不被雨淋湿。\n'
        '要不要带伞呢...收伞好麻烦的，说不定还会忘记拿回家。但是淋雨也不太好...带吗？\n')
talk(text)

choices = {'1' : '还是带上吧，万一下大了就不好了。',
          '2' : '平静的水面培养不出优秀的水手。'}

result = choice(choices)

#第一次选择“带伞”后的分支选项
if result == '1':
    talk('打着伞走在路上，忽然看见一个穿着与你相同款式校服的女生，站在公交站下四处张望。\n'
         '她应该是忘记带伞，不知道该如何是好了。她好像和我是一个学校的，要不要问问呐...\n')

    choices = {'1': '还是算了吧，到时候被当成是什么不良少年就不好了。',
               '2': '问问吧，反正也顺路。'}

    result = choice(choices)

    #选择“带伞”和“帮助”
    if result == '2':
        talk('需要帮忙吗？\n'
            '女生：诶？可以吗？谢谢你！\n'
            '于是顺理成章的，你们一起向着学校走去。\n')
        character_1.affection_up(1)
        character_protagonist.coolness_up(1)

        time.sleep(0.5)
        talk('路上，你们保持着一种微妙的沉默。但直到你们站在同一个教室的门前，才发现你们原来是同班同学。\n'
             '由于途中接上了这个女生，两个人的速度明显慢了下来，所以也很自然的迟到了。\n'
             '虽然迟到了让老师颇有微词，但女生在你身后轻轻扯了扯你的衣领，小声地说了一句谢谢。这让你的心里感到一阵暖流。\n'
             f'座位也只剩下了最后排的两个座位，所以也只能双双落座在那儿了。你不经意间瞟到了女生练习册上的名字：{character_1.full_name}。\n')

    #选择“带伞”和“不帮助”
    else:
        talk('算了，快要迟到了，还是走吧。于是你装作没看到那个女生，急匆匆向学校跑去。\n')

        time.sleep(0.5)
        talk('第一节课的课间，一个女生浑身湿淋淋地走到了你旁边的座位，她的模样跟刚刚站在公交站下的女生如出一辙。你的心里感到有些别扭。\n'
             f'后来，你不经意间瞟到了女生练习册上的名字：{character_1.name}。\n')

#第一次选择“不带伞”后的分支选项
else:
    character_protagonist.coolness_up(1)
    talk('雨下大了，虽然奔跑的过程比较狼狈，但你仍不忘在狼狈中拼命挤出一丝风度。\n'
         '急匆匆跑向学校的途中，你看到一个与你穿着同样款式校服的女生，站在公交车站下四处张望。\n'
         '但再不跑快些就要被雨淋湿了，所以你只能装作没看见，往学校跑去。\n')

    time.sleep(0.5)
    talk('第一节课的课间，一个女生浑身湿淋淋地走到了你旁边的座位，她的模样跟刚刚站在公交站下的女生如出一辙。你的心里稍稍感到有些别扭。\n'
         f'后来，你不经意间瞟到了女生练习册上的名字：{character_1.name}。\n')

#Part 2

date_setting('Mar.20, Thursday', 'Sunny')

time.sleep(0.5)
text = (f'在那之后，你与{character_1.name}基本有一句没一句，彼此之间的共同话题，也仅限于考试之后的互对答案。\n'
        '有天早上上学时，你看到超市外的广告牌上印着一款巧克力的打折CM。你很喜欢吃这个巧克力，但是碍于价格，也只能久久才能忍痛买一板细细品味。\n'
        '看到这个CM，你的内心和包里的零钱都在蠢蠢欲动。于是你买了一块，准备留在今天的自习课上吃。\n'
        '...\n'
        '...\n'
        '终于熬到了自习课，你迫不及待地从抽屉里掏出巧克力。小心翼翼撕开纸包装、打开包裹着的锡箔纸，可可香混杂着果香充斥着鼻腔，你眼中的灼热仿佛能融化眼前的这板巧克力。\n'
        f'一块、两块、三块......一边喝水一边往嘴里送巧克力，仿佛形成了永动机。吃到所剩无几的时候，你的余光不经意间瞟到了{character_1.name}的余光。\n'
        f'你很难看出{character_1.name}眼里满盈的感情：那是种包含着渴望、失落、惆怅、兴奋所融合的目光。\n'
        f'额...要不分给{character_1.name}一块吧...怎么样？\n')
talk(text)

choices = {'1' : '好吧，可能她也还没吃早饭。',
           '2' : '就当没看见吧。毕竟好不容易才买一次:('}

result = choice(choices)

if result == '1' and character_1.affection >= 1:
    talk(f'{character_1.name}：诶？真的嘛！老是麻烦你，真是谢谢啦......嘿嘿⁄(⁄⁄•⁄ω⁄•⁄⁄)⁄\n')
    character_1.affection_up(2)
    character_protagonist.coolness_up(1)

elif result == '1':
    talk(f'{character_1.name}：哇，谢谢喔(｀・ω・´)\n')
    character_1.affection_up(1)
    character_protagonist.coolness_up(1)

else:
    talk('你狼吞虎咽地吃下了这板巧克力，甚至连嘴角融化的巧克力也搜刮得干干净净。\n')

#Part 3

date_setting('Apr.14, Monday', 'Cloudy')

time.sleep(0.5)
text = (f'又是体育课啊...你想着。由于生病，你只能待在教室自习。正当你无所事事四处张望时，看见{character_1.name}的桌上有一本精美的粉色笔记本。\n'
        '你凑近看了看，封皮上赫然写着“日记本”三个字。\n'
        '一股奇怪的想法涌上了你的脑子。走到门外四处张望，大家已经全部下了楼。回到班里，你看着这本日记，你决定：\n')
talk(text)

choices = {'1' : '趁着没人翻开看看。',
           '2' : '还是算了,万一被发现了就不好了。'}

result_special = choice(choices)

if result_special == '2':
    talk('把目光从日记本上挪开后，你感到一阵困意，于是趴在桌上昏昏欲睡。\n'
        f'门外传来的脚步声引起了你的注意，你决定装睡，看看是谁来了。很快，门外出现了{character_1.name}的影子。\n'
        f'她貌似以为我趴在桌上睡着了，便放慢了脚步，轻轻从她的书桌里拿出跳绳。正当我以为她要走了时，{character_1.name}忽然向着我轻轻走了过来，凑近了我的脸。\n'
        f'你只能强装镇定。约莫十秒后，你感受到{character_1.name}的脚步声渐渐远离了教室。\n'
         '虽然空气中逐渐安静了下来，但你的心跳并没有因此而舒缓下来。\n')
    character_1.affection_up(3)
    character_protagonist.coolness_up(1)

elif result_special == '1' and character_1.affection == 0:
    talk('日记里写着一位少女该有的模样：时不时兴起的小情绪、想吃的甜品、去过的城市......\n'
        f'正当你看得津津有味时，门外传来{character_1.name}带着愠气的声音：“你在做什么呢！要不是我跳绳忘记拿了，都看不出你是这样的人！有没有一点好！\n”'
        f'{character_1.name}丝毫没有给我解释的机会，一把从我手中夺走了笔记本，带着哭腔离开了。\n'
        f'后来{character_1.name}找班主任调到了离我很远的位置，整个高中三年，我与{character_1.name}就像是陌生人一般，失去了任何纽带。\n')

    time.sleep(1)
    talk('游戏结束，希望下次有个更好的结果...')
    sys.exit()

elif result_special == '1' and 0 < character_1.affection <= 1:
    talk('日记里写着一位少女该有的模样：时不时兴起的小情绪、想吃的甜品、去过的城市......'
        f'在某一页的纸上，{character_1.name}写着：“今天，隔壁桌的男生给我分了一半巧克力，那种巧克力我很喜欢吃，但是价格太贵啦！谢谢他分享给我。'
        f'正当你看得津津有味时，门外传来{character_1.name}带着愠气的声音：“你干嘛！'
        f'你急忙合上笔记本，连声道歉。{character_1.name}脸上浮现出生气的表情，转头离开了。\n')
    character_1.affection_down(2)
    character_protagonist.coolness_down(1)

elif result_special == '1' and character_1.affection > 1:
    talk('日记里写着一位少女该有的模样：时不时兴起的小情绪、想吃的甜品、去过的城市......\n'
        f'在某一页的纸上，{character_1.name}写着：“隔壁桌的男生之前好心来带没伞的我到学校，前几天还分了我一半巧克力诶！\n'
        '那个巧克力好贵喔，每次我都舍不得买...我好像有点...>_<！！\n'
        f'正当你看得津津有味时，门外传来{character_1.name}的声音：嗯？你在做什么？\n'
        f'你急忙合上笔记本，连声道歉。{character_1.name}脸上浮现出复杂的表情，转头离开了。\n')
    character_1.affection_down(2)
    character_protagonist.coolness_down(1)

#Part 4

date_setting('May.16, Friday', 'Sunny')

time.sleep(0.5)

text = (f'之后，你与{character_1.name}通过同学群聊加上了好友，虽然在线上两人聊得有来有回的，但线下在学校时，彼此间的话语却变得越来越少。\n'
        f'周五，又轮到你和{character_1.name}值日了。你漫不经心地拿着扫把摸鱼，看到她拿着板擦，拼命地踮起脚尖，却怎么也够不到最上面的粉笔字。\n'
        f'于是你：\n')
talk(text)

choices = {'1' : '忍不住盯着她的背影偷笑',
           '2' : '把头背过去偷笑',
           '3' : '还是帮她擦一下吧...'}

result = choice(choices)

if result == '1':
    if character_1.affection >= 4:
        talk(f'{character_1.name}像是听到了声音，将头转了过来，正好对上了我的眼神。\n'
             f'看到我的表情后，{character_1.name}的脸上顿时浮现出了潮红，拿着板擦的手不知道该如何是好，只能僵硬地举在空中。\n'
             f'还真是令人尴尬的时刻啊...过了两秒后，{character_1.name}小声地嘟囔道：别看了...那，那帮我擦一下咯...啊哈哈...\n'
             f'你看着{character_1.name}的表情，也开始觉得有点不好意思起来。快步走上讲台，接过{character_1.name}里的板擦，她的手软软的、很光滑。\n'
             f'三两下把黑板擦干净，你们又陷入到了微妙的沉默中。{character_1.name}的眼睛一直盯着地板，抢一步开口说道：谢谢啦...那，我先走啦？\n'
             f'哦，哦...你只能勉强应和道。{character_1.name}便走向她的座位，开始收拾起书包，动作慢到像是开了0.5倍速，仿佛每一个动作都是精心排练过的舞蹈动作。\n'
             f'拜拜！{character_1.name}说道。好...你朝她挥了挥手。站在讲台上，你看着千夏的背影一步步远离，最终消失在走廊的拐角。\n'
             f'转过拐角时，{character_1.name}不经意间朝你的方向看了一眼，你们的目光再一次交接。当你意识到这点时，她已经不见人影了。\n')
        character_1.affection_up(2)

    else:
        talk(f'{character_1.name}像是听到了声音，将头转了过来，正好对上了我的眼神。\n'
             f'看到我的表情后，{character_1.name}的脸上顿时浮现出了潮红，拿着板擦的手不知道该如何是好，只能僵硬地举在空中。\n'
             f'还真是令人尴尬的时刻啊...过了两秒后，{character_1.name}小声地嘟囔道：笑什么笑啦，真的是...那帮我擦一下咯...\n'
             f'你看着{character_1.name}的表情，也开始觉得有点不好意思起来。快步走上讲台，接过{character_1.name}里的板擦，'
             f'三两下把黑板擦干净，{character_1.name}抢一步开口说道：谢谢啦...那，我先走啦？\n'
             f'哦，哦...你只能勉强应和道。{character_1.name}拿起书包，朝我挥了挥手。站在讲台上，你看着千夏的背影一步步远离，最终消失在走廊的拐角。\n')
        
elif result == '2':
    talk(f'{character_1.name}像是听到了声音，将头转了过来。看到你的背影不停地抽搐，她有些担心的问：那个，{character_protagonist.full_name}，感冒了吗？\n'
         f'听到这话，你一时间收起了笑容。背对着她，你小声地回了一句：没有没有，谢谢啦。\n'
         f'{character_1.name}不知道你是什么意思，只能嗯嗯地应道。\n')
    
    if random.random() < 0.5 + float(character_protagonist.coolness) * 0.1:
        character_1.affection_up(2)
    else:
        character_1.affection_down(1)


else:
    talk('你走上讲台，轻声问道：姐，要不我来吧？\n'
         f'{character_1.name}貌似没有察觉到你的脚步，听到你的声音时，浑身瑟缩了一下。她不好意思地别过头去，用比你更小声的声音应道：嗯,谢谢啦...\n'
         f'三两下把黑板擦干净，{character_1.name}抢一步开口说道：谢谢啦...那，我先走啦？\n'
         f'哦，哦...你只能勉强应和道。{character_1.name}拿起书包，朝我挥了挥手。站在讲台上，你看着千夏的背影一步步远离，最终消失在走廊的拐角。\n')
    character_1.affection_up(2)
    character_protagonist.coolness_up(1)

#Part 5

date_setting('Jun.27, Friday', 'Sunny')

time.sleep(0.5)

text = (f'随着你与{character_1.name}间的关系越来越近，加上她安静温柔的性格所带来的温暖逐渐充斥了你的生活，你觉得自己貌似有点喜欢上{character_1.name}了。\n'
        f'你决定在今天期末考试结束后，向{character_1.name}说明自己的心意。\n'
        '...\n'
        '...\n'
        f'最后的铃声响起，考试结束了。你将{character_1.name}约在了黄昏无人的教室。\n'
        f'夕阳将{character_1.name}的侧脸映照得很美。看着她不解的眼神，你决定趁现在说出你的告白：')

talk(text)

confession_lines = input()

time.sleep(random.uniform(1, 5))

if character_1.affection >= 5:
    if result_special == '2':
        if random.random() < 0.4 + float(character_protagonist.coolness) * 0.1:
            talk(f'听到你的话，{character_1.name}的脸变得通红。约莫五秒后，{character_1.name}沉默着仰起头，双手背在身后。此时的你：\n')

            choices = {'1' : '亲她',
                       '2' : '亲她',
                       '3' : '亲她'}
            
            choice(choices)

            talk(f'你与{character_1.name}在黄昏中亲吻，久久不愿睁眼。\n')

            time.sleep(5.2)

        else:
            talk(f'听到你的话,{character_1.name}的脸上浮现出一种复杂的神色，像是犹豫、悲伤和生气几种情绪交织融合。约莫五秒后，她沉默地离开了。\n')

    else:
        talk(f'听到你的话，{character_1.name}的脸变得通红。约莫五秒后，{character_1.name}沉默着仰起头，双手背在身后。此时的你：\n')

        choices = {'1' : '亲她',
                       '2' : '亲她',
                       '3' : '亲她'}
            
        choice(choices)

        talk(f'你与{character_1.name}在黄昏中亲吻，久久不愿睁眼。\n')

        time.sleep(5.2)

elif 0 <= character_1.affection < 5:
    if result_special == '2':
        talk(f'听到你的话,{character_1.name}的脸上浮现出一种复杂的神色，像是犹豫、悲伤和生气几种情绪交织融合。约莫五秒后，她沉默地离开了。\n')

    else:
        if random.random() < 0.4 + character_1.affection:
            talk('\n听到你的话，千夏的脸变得通红。约莫五秒后，千夏缓缓开口：“我，可是很麻烦的哦？”')

        else:
            talk(f'听到你的话,{character_1.name}的脸上浮现出一种复杂的神色，像是犹豫、悲伤和生气几种情绪交织融合。约莫五秒后，她沉默地离开了。\n')

else:
    talk(f'听到你的话,{character_1.name}的脸上毫无波澜。约莫五秒后，她消失在了教室的门口。\n')

time.sleep(2)

talk('谢谢游玩！')
      



        



