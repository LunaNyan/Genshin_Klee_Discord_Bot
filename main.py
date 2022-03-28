import sys, os, discord, configparser, logging, traceback, time, random, math
from datetime import datetime

sys.path.append("./modules/")
import toolbox, helps, gacha, stats, selector, characters
sys.path.append("./gacha_data/")
import metadata
sys.path.append("../../")

global bot_ver
bot_ver = "LIVE-20220213-FINAL"

print("INFO    : Klee Discord bot, version " + bot_ver)

try: # config 불러오기
    conf = configparser.ConfigParser()
    conf_path = "config"
    conf.read(conf_path)
    print("INFO    : Configuration file loaded")
except Exception as e:
    print("FATAL   : Couldn't load configuration file : " + str(e))
    sys.exit(1)

# db 불러오기
db = configparser.ConfigParser()
db_path = "db/db.dat"
db.read(db_path)
print("INFO    : DB file loaded")

# 로거 생성
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

# 봇 클라이언트 할당
client = discord.Client()

# 공지사항 전달
async def announce(message, embed):
    await message.channel.send("Sending announcement..")
    embed.set_thumbnail(url=client.user.avatar_url)
    if a_imgurl != "" or a_imgurl != "none":
        embed.set_image(url=a_imgurl)
    chs = []
    for i in db.items("announcement_channel"):
        try:
            if i[1].startswith("_"):
                c = int(i[1].replace("_", ""))
            else:
                c = int(i[1])
            news_channel = client.get_channel(c)
            await news_channel.send(embed=embed)
            await message.channel.send(":green_square: " + news_channel.name + " at " + news_channel.guild.name + " (" + str(i[1]) + " at " + str(i[0]) + ") : Success")
        except Exception as e:
            db.remove_option("announcement_channel", i[0])
            await message.channel.send(":red_square: " + str(i[1]) + " : Failed (" + str(e) + ")")
    await message.channel.send("Complete")

# 공지사항 blob 생성
a_title = ""
a_content = ""
a_imgurl = ""

# 봇 계정으로 로그인 완료 시
@client.event
async def on_ready():
    print('INFO    : Bot is ready to use.')
    print("INFO    : Account : " + str(client.user.name) + "(" + str(client.user.id) + ")")
    await client.change_presence(activity=discord.Game("!도움 | ver " + bot_ver))

# 명령어
@client.event
async def on_message(message):
    global a_title, a_content, a_imgurl
    try:
        # 봇이 명령어를 입력한 경우 무시
        if message.author == client.user:
            # !! 이 코드는 항상 최상단에 둘것 !!
            return
        # 유저 데이터 없을 시 만들기
        try:
            db.get(str(message.author.id), "config")
        except:
            db.add_section(str(message.author.id))
            toolbox.init_userdata_config(db, message)
        # 서버 관리자인지 체크
        try:
            if str(message.author.id) in conf.get("config", "owner_id"):
                ifadmin = True
            elif message.author.guild_permissions.administrator:
                ifadmin = True
            else:
                ifadmin = False
        except:
            ifadmin = False
        # 커스텀 접두어 체크
        try:
            head = db.get("custom_head", str(message.guild.id))
        except:
            head = "!"
        # 일반 커맨드
        if message.content.startswith("!도움"):
            await message.reply(embed=helps.help("!", message, bot_ver, ifadmin, head))
        elif head != "!" and message.content.startswith(head + "도움"):
            await message.reply(embed=helps.help(head, message, bot_ver, ifadmin))
        elif message.content.startswith(head + "용어"):
            await message.reply(embed=helps.helpg(head, message))
        elif message.content == head + "이용약관":
            await message.reply(embed=helps.tos())
        elif message.content == head + "제작자":
            await message.reply(embed=helps.credits(client, bot_ver))
        elif message.content == head + "재료":
            await message.reply(embed=toolbox.dailyresin())
        elif message.content.startswith(head + "기원"):
            if message.content == head + "기원":
                await message.reply(embed=selector.gacha_list(db, message))
            else:
                try:
                    res = selector.select_gacha(db, message)
                    embed=discord.Embed(title="기원을 " + res + "(으)로 선택했어!")
                except ValueError:
                    text = "기원 번호는 " + head + "기원, " + head + "목록에서 확인할 수 있습니다"
                    embed=discord.Embed(title="없는 번호의 기원이야!", description=text)
                await message.reply(embed=embed)
        elif message.content.startswith(head + "목록"):
            await message.reply(embed=selector.gacha_list_detailed(message))
        elif message.content in [head + "단차", head + "단챠"]:
            res = gacha.do_gacha(db, message)
            if res[1][0][0] == 5:
                scor = 0xffff00
            elif res[1][0][0] == 4:
                scor = 0x9966cc
            else:
                scor = 0x0099cc
            embed=discord.Embed(title=res[2][0] + "회차 : " + toolbox.preetify(res[1][0]), color=scor)
            stack = stats.stacks(db, message)
            embed.set_footer(text="현재 기원 : " + res[0][0] + "\n5성 스택 : " + stack)
            await message.reply(embed=embed)
        elif message.content in [head + "연차", head + "연챠"]:
            res = gacha.do_gacha(db, message, amount=10)
            stars = []
            t = ""
            tries = res[4] - res[3] + 1
            for s in res[1]:
                stars.append(s[0])
                t += str(tries) + "회차 : " + toolbox.preetify(s, mode=True) + "\n"
                tries += 1
            if 5 in stars:
                scor = 0xffff00
            elif 4 in stars:
                scor = 0x9966cc
            else:
                scor = 0x0099cc
            embed = discord.Embed(title="10연차 결과", description=t, color=scor)
            stack = stats.stacks(db, message)
            embed.set_footer(text="현재 기원 : " + res[0][0] + "\n5성 스택 : " + stack)
            await message.reply(embed=embed)
        elif message.content == head + "천장":
            dbi = toolbox.getFromList(db, str(message.author.id), "config")
            if dbi[1] == "1":
                stats.reset(db, message)
            res = gacha.do_gacha(db, message, mode=1)
            resn = res[1][-1][2]
            embed = discord.Embed(title=str(res[4]) + "회차 (" + str(res[3]) + "스택)에 " + resn + toolbox.checkTrait(resn) + " 뽑혔어!", color=0xffff00)
            if res[5] != None:
                embed = discord.Embed(title=str(res[4]) + "회차 (" + str(res[7]) + "스택)에 " + resn + toolbox.checkTrait(resn) + " 뽑혔어!", color=0xffff00)
                if dbi[0] != "S0100":  # 상시 픽업은 픽뚫이 존재하지 않음
                    embed.add_field(name="비 픽업 5성 아이템 획득 : " + res[5][2], value="회차 : " + str(res[6][0]) + " (" + str(res[6][1]) + "스택)")
            else:
                embed = discord.Embed(title=str(res[4]) + "회차 (" + str(res[3]) + "스택)에 " + resn + toolbox.checkTrait(resn) + " 뽑혔어!", color=0xffff00)
            if dbi[1] == "1":
                embed.set_footer(text="현재 기원 : " + res[0][0] + ", 자동 리셋 켜짐")
            else:
                embed.set_footer(text="현재 기원 : " + res[0][0])
            await message.reply(embed=embed)
            fn = toolbox.saveToFile(db, message, res)
            await message.reply(file=discord.File(fn))
            os.remove(fn)
        elif message.content.startswith(head + "저격") or message.content.startswith(head + "명함"):
            if message.content == head + "저격" or message.content == head + "명함":
                embed=discord.Embed(title="사용 방법 : " + head + "저격 (이름) 또는 " + head + "명함 (이름)")
                await message.reply(embed=embed)
            else:
                try:
                    if "!저격" in message.content:
                        m = message.content.replace(head + "저격 ", "")
                    else:
                        m = message.content.replace(head + "명함 ", "")
                    try:
                        m1 = characters.alias(m)
                        m = m1
                        m1 = None # 메모리 누수 방지
                    except NameError:
                        pass
                    dbi = toolbox.getFromList(db, str(message.author.id), "config")
                    if dbi[1] == "1":
                        stats.reset(db, message)
                    try:
                        res = gacha.do_gacha(db, message, snipeFor=m)
                    except NameError:
                        selector.select_gacha_intl(db, message, metadata.get_pickup_name(m))
                        res = gacha.do_gacha(db, message, snipeFor=m)
                    resn = res[1][-1][2]
                    if res[5] != None:
                        embed = discord.Embed(title=str(res[4]) + "회차 (" + str(res[7]) + "스택)에 " + resn + toolbox.checkTrait(resn) + " 뽑혔어!", color=0xffff00)
                        if dbi[0] != "S0100": # 상시 픽업은 픽뚫이 존재하지 않음
                            embed.add_field(name="비 픽업 5성 아이템 획득 : " + res[5][2], value="회차 : " + str(res[6][0]) + " (" + str(res[6][1]) + "스택)")
                    else:
                        embed = discord.Embed(title=str(res[4]) + "회차 (" + str(res[3]) + "스택)에 " + resn + toolbox.checkTrait(resn) + " 뽑혔어!", color=0xffff00)
                    if dbi[1] == "1":
                        embed.set_footer(text="현재 기원 : " + res[0][0] + ", 자동 리셋 켜짐")
                    else:
                        embed.set_footer(text="현재 기원 : " + res[0][0])
                    await message.reply(embed=embed)
                    fn = toolbox.saveToFile(db, message, res)
                    await message.reply(file=discord.File(fn))
                    os.remove(fn)
                except NameError:
                    tit = "찾을 수 없는 항목이야!"
                    embed = discord.Embed(title=tit)
                    text = "본명을 그대로 사용하는 캐릭터의 경우 편의를 위해 줄인 이름으로 등록되어 있습니다.\n(예시 : 카에데하라 카즈하 → 카즈하)"
                    embed.add_field(name="이름에 오탈자가 있는지 확인해주세요.", value=text, inline=False)
                    text = "'!기원'을 입력해 주요 기원 목록을 확인할 수 있습니다."
                    embed.add_field(name="올바른 기원을 선택했는지 확인해주세요.", value=text, inline=False)
                    dbi = toolbox.getFromList(db, str(message.author.id), "config")
                    embed.set_footer(text="현재 선택된 기원 : " + metadata.get_gacha_name(dbi[0]))
                    await message.reply(embed=embed)
        elif message.content.startswith(head + "풀돌"):
            if message.content == head + "풀돌":
                embed=discord.Embed(title="사용 방법 : " + head + "풀돌 (이름)")
                await message.reply(embed=embed)
            else:
                try:
                    m = message.content.replace(head + "풀돌 ", "")
                    try:
                        m1 = characters.alias(m)
                        m = m1
                        m1 = None # 메모리 누수 방지
                    except NameError:
                        pass
                    dbi = toolbox.getFromList(db, str(message.author.id), "config")
                    if dbi[1] == "1":
                        stats.reset(db, message)
                    try:
                        res = gacha.do_gacha(db, message, snipeFor=m, c_amounts=7)
                    except NameError:
                        selector.select_gacha_intl(db, message, metadata.get_pickup_name(m))
                        res = gacha.do_gacha(db, message, snipeFor=m, c_amounts=7)
                    resn = res[1][-1][2]
                    embed = discord.Embed(title=str(res[4]) + "회차를 끝으로 " + resn + "의 풀돌을 완료혔어!", color=0xffff00)
                    if dbi[1] == "1":
                        embed.set_footer(text="현재 기원 : " + res[0][0] + ", 자동 리셋 켜짐")
                    else:
                        embed.set_footer(text="현재 기원 : " + res[0][0])
                    await message.reply(embed=embed)
                    fn = toolbox.saveToFile(db, message, res)
                    await message.reply(file=discord.File(fn))
                    os.remove(fn)
                except NameError:
                    tit = "찾을 수 없는 항목이야!"
                    embed = discord.Embed(title=tit)
                    text = "본명을 그대로 사용하는 캐릭터의 경우 편의를 위해 줄인 이름으로 등록되어 있습니다.\n(예시 : 카에데하라 카즈하 → 카즈하)"
                    embed.add_field(name="이름에 오탈자가 있는지 확인해주세요.", value=text, inline=False)
                    text = "'!기원'을 입력해 주요 기원 목록을 확인할 수 있습니다."
                    embed.add_field(name="올바른 기원을 선택했는지 확인해주세요.", value=text, inline=False)
                    dbi = toolbox.getFromList(db, str(message.author.id), "config")
                    embed.set_footer(text="현재 선택된 기원 : " + metadata.get_gacha_name(dbi[0]))
                    await message.reply(embed=embed)
        elif message.content in [head + "반천장", head + "5성"]:
            dbi = toolbox.getFromList(db, str(message.author.id), "config")
            if dbi[1] == "1":
                stats.reset(db, message)
            res = gacha.do_gacha(db, message, mode=2)
            resn = res[1][-1][2]
            embed = discord.Embed(title=str(res[3]) + "회차에 " + resn + toolbox.checkTrait(resn) + " 뽑혔어!", color=0xffff00)
            if res[5] != None:
                embed = discord.Embed(title=str(res[4]) + "회차 (" + str(res[7]) + "스택)에 " + resn + toolbox.checkTrait(resn) + " 뽑혔어!", color=0xffff00)
                if dbi[0] != "S0100":  # 상시 픽업은 픽뚫이 존재하지 않음
                    embed.add_field(name="비 픽업 5성 아이템 획득 : " + res[5][2], value="회차 : " + str(res[6][0]) + " (" + str(res[6][1]) + "스택)")
            else:
                embed = discord.Embed(title=str(res[4]) + "회차 (" + str(res[3]) + "스택)에 " + resn + toolbox.checkTrait(resn) + " 뽑혔어!", color=0xffff00)
            if dbi[1] == "1":
                embed.set_footer(text="현재 기원 : " + res[0][0] + ", 자동 리셋 켜짐")
            else:
                embed.set_footer(text="현재 기원 : " + res[0][0])
            await message.reply(embed=embed)
            fn = toolbox.saveToFile(db, message, res)
            await message.reply(file=discord.File(fn))
            os.remove(fn)
        elif message.content == head + "통계":
            await message.reply(embed=stats.stats(db, message))
        elif message.content.startswith(head + "견적"):
            if message.content == head + "견적":
                gems_preowned = 0
            else:
                try:
                    m = message.content.replace(head + "견적 ", "")
                    gems_preowned = int(m)
                except:
                    gems_preowned = 0
            dbi = toolbox.getFromList(db, str(message.author.id), "config")
            try:
                dbs = toolbox.getFromList(db, str(message.author.id), "gacha_" + dbi[0])
            except:
                toolbox.init_userdata_gacha(db, message, dbi[0])
                dbs = toolbox.getFromList(db, str(message.author.id), "gacha_" + dbi[0])
            cnt = int(dbs[0])
            embed = stats.estimate(cnt, gems_preowned)
            embed.set_footer(text="현재 선택된 기원 : " + metadata.get_gacha_name(dbi[0]))
            await message.reply(embed=embed)
        elif message.content.startswith(head + "스택"):
            await message.reply(embed=stats.set_stack(db, message))
        elif message.content.startswith(head + "캐릭터"):
            if message.content == head + "캐릭터":
                embed = discord.Embed(title="사용 방법 : " + head + "캐릭터 (캐릭터명)")
            else:
                m = message.content.replace(head + "캐릭터 ", "")
                try:
                    embed = characters.search_char(m)
                except NameError:
                    embed = discord.Embed(title="찾을 수 없는 항목이야!", description="이름에 오탈자가 있는지 확인해주세요.")
            await message.reply(embed=embed)
        elif message.content.startswith(head + "레진"):
            if message.content == head + "레진":
                embed=discord.Embed(title="사용 방법 : " + head + "레진 (레진 잔량)")
            else:
                try:
                    m = int(message.content.replace(head + "레진 ", ""))
                    embed=toolbox.resin(m, message, db)
                except:
                    embed=discord.Embed(title="사용 방법 : " + head + "레진 (레진 잔량)")
            await message.reply(embed=embed)
        elif message.content == head + "정보":
            await message.reply(embed=selector.gacha_info(db, message))
        elif message.content in ["!리셋", "!초기화"]:
            await message.reply(embed=stats.reset(db, message))
        elif message.content == head + "자동리셋":
            dbi = toolbox.getFromList(db, str(message.author.id), "config")
            if dbi[1] == "0":
                dbi[1] = "1"
                embed = discord.Embed(title="이제 천장, 반천장 명령어를 쓰기 전에 통계를 초기화할게!")
            else:
                dbi[1] = "0"
                embed = discord.Embed(title="천장, 반천장 통계 초기화를 해제했어!")
            toolbox.setToList(db, str(message.author.id), "config", dbi)
            await message.reply(embed=embed)
        elif message.content == head + "3성":
            dbi = toolbox.getFromList(db, str(message.author.id), "config")
            try:
                if dbi[2] == "1":
                    dbi[2] = "0"
                    embed = discord.Embed(title="출력 파일에 3성 아이템 정보를 제외할게!")
                else:
                    dbi[2] = "1"
                    embed = discord.Embed(title="출력 파일에 3성 아이템 정보를 포함할게!")
                toolbox.setToList(db, str(message.author.id), "config", dbi)
            except:
                dbi.append("1")
                toolbox.setToList(db, str(message.author.id), "config", dbi)
                embed = discord.Embed(title="출력 파일에 3성 아이템 정보를 포함할게!")
            await message.reply(embed=embed)
        elif message.content == head + "시간제":
            dbi = toolbox.getFromList(db, str(message.author.id), "config")
            try:
                if dbi[3] == "1":
                    dbi[3] = "0"
                    embed = discord.Embed(title="시간 표시 방식을 24시간제로 바꿨어!")
                else:
                    dbi[3] = "1"
                    embed = discord.Embed(title="시간 표시 방식을 12시간제로 바꿨어!")
                toolbox.setToList(db, str(message.author.id), "config", dbi)
            except:
                dbi.append("1")
                toolbox.setToList(db, str(message.author.id), "config", dbi)
                embed = discord.Embed(title="시간 표시 방식을 12시간제로 바꿨어!")
            await message.reply(embed=embed)
        # 팀원 커맨드
        elif message.content.startswith("!dsay") and message.author.id == int(conf.get("config", "owner_id")):
            m = message.content.replace("!dsay ", "")
            await message.channel.send(m)
        elif message.content.startswith("!a_title") and message.author.id == int(conf.get("config", "owner_id")):
            m = message.content.replace("!a_title ", "")
            a_title = m
            await message.channel.send(":ok_hand:")
        elif message.content.startswith("!a_content") and message.author.id == int(conf.get("config", "owner_id")):
            m = message.content.replace("!a_content ", "")
            a_content = m
            await message.channel.send(":ok_hand:")
        elif message.content.startswith("!a_imgurl") and message.author.id == int(conf.get("config", "owner_id")):
            m = message.content.replace("!a_imgurl ", "")
            a_imgurl = m
            await message.channel.send(":ok_hand:")
        elif message.content == "!asend" and message.author.id == int(conf.get("config", "owner_id")):
            embed=discord.Embed(title=a_title, description=a_content)
            if a_imgurl != "" or a_imgurl != "none":
                embed.set_image(url=a_imgurl)
            await announce(message, embed)
        elif message.content == "!apreview":
            embed=discord.Embed(title=a_title, description=a_content)
            if a_imgurl != "" or a_imgurl != "none":
                embed.set_image(url=a_imgurl)
            await message.channel.send(embed=embed)
        # 서버 관리자 커맨드
        elif message.content == head + "공지채널" and ifadmin:
            db.set("announcement_channel", str(message.guild.id), str(message.channel.id))
            embed = discord.Embed(title="공지사항 게시 채널을 지정했습니다. 봇과 관련된 공지사항 게시는 이 채널로 고정됩니다.")
            await message.reply(embed=embed)
        elif message.content.startswith(head + "접두어") and ifadmin:
            if message.content == head + "접두어":
                embed=discord.Embed(title="사용 방법 : !접두어 (접두어)")
            else:
                m = message.content.replace(head + "접두어 ", "")
                db.set("custom_head", str(message.guild.id), m)
                embed = discord.Embed(title="접두어를 설정했습니다. 모든 명령어는 " + m + "으로 시작합니다.")
                embed.set_footer(text="오류 발생 시 '!접두어초기화'를 입력하세요.")
            await message.reply(embed=embed)
        elif message.content == "!접두어초기화" and ifadmin:
            db.remove_option("custom_head", str(message.guild.id))
            embed = discord.Embed(title="접두어를 초기화했습니다.")
            await message.reply(embed=embed)
        # 공지사항 채널 지정
        else:
            try:
                try:
                    xx = db.get("announcement_channel", str(message.guild.id))
                    if xx.startswith("_"):
                        db.set("announcement_channel", str(message.guild.id), "_" + str(message.channel.id))
                    else:
                        pass
                except:
                    db.set("announcement_channel", str(message.guild.id), "_" + str(message.channel.id))
            except: # 봇 간 DM방에서 명령어 사용 시, 공지사항 채널로 지정하지 않음
                pass
    # 오류 핸들러
    except Exception as e:
        if "Missing Permissions" in str(e):
            await message.reply('권한이 부족합니다. "링크 첨부"와 "파일 첨부" 권한을 활성화해주세요.')
        else:
            embed=discord.Embed(title="뭔가 잘못되었나 봐!", description="오류 내용 : " + str(e) + "\n클레가 오류 보고서를 전송해 놨으니까 곧 고쳐질거야!")
            await message.reply(embed=embed)
            if "루프가 허용 한도를 초과했습니다." in str(e):
                pass
            else:
                cid = conf.get("config", "traceback_channel")
                cid = client.get_channel(int(cid))
                embed = discord.Embed(title="Traceback occured at " + str(datetime.now()))
                embed.add_field(name="Traceback", value="```" + traceback.format_exc() + "```")
                try:
                    embed.add_field(name="user", value="```" + message.author.name + " (" + str(message.author.id) + ")```", inline=False)
                    embed.add_field(name="guild", value="```" + message.guild.name + " (" + str(message.guild.id) + ")```", inline=False)
                    embed.add_field(name="channel", value="```" + message.channel.name + " (" + str(message.channel.id) + ")```", inline=False)
                except:
                    pass
                embed.add_field(name="message content", value="```" + message.content + "```", inline=False)
                await cid.send(embed=embed)
    with open(db_path, 'w') as configfile:
        db.write(configfile)

@client.event
async def on_guild_join(guild):
    if guild.system_channel != None:
        await guild.system_channel.send(embed=helps.welcome_message(client, bot_ver))

print("INFO    : connecting to Discord. Please Wait..")
client.run(conf.get("config", "bot_token"))
