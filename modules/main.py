import sys, os, discord, configparser, logging, traceback, time, random, math
import m_gacha_pull, m_help, m_estimate, m_search, m_etc
from datetime import datetime
sys.path.append('../gacha_data/')
import pickup_character, pickup_weapon, anytime
sys.path.append('../')

global bot_ver
bot_ver = "0.90"

print("INFO    : Klee Discord bot, version " + bot_ver)
print("INFO    : Pickup character data : " + pickup_character.data_name + " (ver " + pickup_character.data_ver + ")")
print("INFO    : Pickup weapon data    : " + pickup_weapon.data_name + " (ver " + pickup_weapon.data_ver + ")")
print("INFO    : Anytime data          : " + anytime.data_name + " (ver " + anytime.data_ver + ")")

try: # config 불러오기
    conf = configparser.ConfigParser()
    conf_path = "config.ini"
    conf.read(conf_path)
    print("INFO    : Configuration file loaded")
except Exception as e:
    print("FATAL   : Couldn't load configuration file : " + str(e))
    sys.exit(1)

# db 불러오기
db = configparser.ConfigParser()
db_path = "../db/db.dat"
db.read(db_path)
print("INFO    : DB file loaded")

logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

client = discord.Client()

@client.event
async def on_ready():
    print('INFO    : Bot is ready to use.')
    print("INFO    : Account : " + str(client.user.name) + "(" + str(client.user.id) + ")")
    await client.change_presence(activity=discord.Game("!도움 | ver " + bot_ver))

@client.event
async def on_message(message):
    try:
        if message.author == client.user:
            # !! 이 코드는 항상 최상단에 둘것 !!
            return
        if not db.has_section(str(message.author.id)):
            # db에 해당 유저 섹션이 없는 경우 structure initialize 처리
            db.add_section(str(message.author.id))
            db.set(str(message.author.id), "gacha_mode", "1")
            for i in range(3):
                db.set(str(message.author.id), "stack_5star_pull_" + str(i + 1), "0")
                db.set(str(message.author.id), "stack_4star_pull_" + str(i + 1), "0")
                if i != 2:
                    db.set(str(message.author.id), "stack_5star_nothope_" + str(i + 1), "0")
                    db.set(str(message.author.id), "stack_4star_nothope_" + str(i + 1), "0")
                    db.set(str(message.author.id), "total_nothope_" + str(i + 1), "0")
                db.set(str(message.author.id), "total_pull_" + str(i + 1), "0")
                db.set(str(message.author.id), "total_5star_" + str(i + 1), "0")
                db.set(str(message.author.id), "total_4star_" + str(i + 1), "0")
                db.set(str(message.author.id), "total_3star_" + str(i + 1), "0")
                db.set(str(message.author.id), "total_character_" + str(i + 1), "0")
                db.set(str(message.author.id), "total_item_" + str(i + 1), "0")
        # 자동리셋 여부 확인
        try:
            autoreset = db.get(str(message.author.id), "autoreset")
        except:
            db.set(str(message.author.id), "autoreset", "0")
            autoreset = "0"
        # 일반 커맨드
        if message.content == "!도움":
            await message.channel.send(embed=m_help.help(bot_ver))
        if message.content == "!이용약관":
            await message.channel.send(embed=m_help.tos())
        if message.content == "!제작자":
            await message.channel.send(embed=m_help.credits(client, bot_ver))
        elif message.content == "!버전":
            embed = discord.Embed(title="버전 정보")
            embed.add_field(name="봇 버전", value=bot_ver)
            embed.add_field(name="캐릭터 픽업 기원 데이터", value=pickup_character.data_name + " (ver " + pickup_character.data_ver + ")", inline=False)
            embed.add_field(name="무기 픽업 기원 데이터", value=pickup_weapon.data_name + " (ver " + pickup_weapon.data_ver + ")", inline=False)
            embed.add_field(name="상시 기원 데이터", value=anytime.data_name + " (ver " + anytime.data_ver + ")", inline=False)
            await message.channel.send(embed=embed)
        elif message.content.startswith("!기원"):
            if message.content == "!기원":
                try:
                    gm = db.get(str(message.author.id), "gacha_mode")
                    if gm == "1":
                        embed = discord.Embed(title="현재 캐릭터 픽업 기원이 선택되어 있어!")
                    elif gm == "2":
                        embed = discord.Embed(title="현재 무기 픽업 기원이 선택되어 있어!")
                    elif gm == "3":
                        embed = discord.Embed(title="현재 상시 기원이 선택되어 있어!")
                    else:
                        raise
                except:
                    embed = discord.Embed(title="기원 목록")
                embed.add_field(name="#1 : " + pickup_character.data_name, value="캐릭터 픽업 기원")
                embed.add_field(name="#2 : " + pickup_weapon.data_name, value="무기 픽업 기원")
                embed.add_field(name="#3 : " + anytime.data_name, value="상시 기원")
            else:
                if message.content == "!기원 1":
                    db.set(str(message.author.id), "gacha_mode", "1")
                    embed = discord.Embed(title="캐릭터 픽업으로 기원 모드를 바꿨어!")
                elif message.content == "!기원 2":
                    db.set(str(message.author.id), "gacha_mode", "2")
                    embed = discord.Embed(title="무기 픽업으로 기원 모드를 바꿨어!")
                elif message.content == "!기원 3":
                    db.set(str(message.author.id), "gacha_mode", "3")
                    embed = discord.Embed(title="상시 기원으로 기원 모드를 바꿨어!")
                else:
                    embed = discord.Embed(title="어떤 기원이었더라? 클레는 모르겠어...")
            await message.channel.send(embed=embed)
        elif message.content == "!단차" or message.content == "!단챠":
            resc = m_gacha_pull.descript_pull(m_gacha_pull.pull(db, message))
            embed = discord.Embed(title=str(m_gacha_pull.get_stat(db, message)[0]) + "회차 : " + resc)
            if db.get(str(message.author.id), "gacha_mode") == "1":
                f_text = "현재 기원 : 캐릭터 픽업"
            elif db.get(str(message.author.id), "gacha_mode") == "2":
                f_text = "현재 기원 : 무기 픽업"
            else:
                f_text = "현재 기원 : 상시 기원"
            embed.set_footer(text=f_text)
            await message.channel.send(embed=embed)
        elif message.content == "!연차" or message.content == "!연챠":
            await message.channel.trigger_typing()
            encountered_5star = False
            rest = ""
            for _ in range(10):
                resi = m_gacha_pull.pull(db, message)
                resc = m_gacha_pull.descript_pull(resi)
                if resi[0] == 5:
                    encountered_5star = True
                rest += str(m_gacha_pull.get_stat(db, message)[0]) + "회차 : " + resc + "\r\n"
            if encountered_5star:
                embed = discord.Embed(title="10연차 결과", description=rest, color=0xffff00)
            else:
                embed = discord.Embed(title="10연차 결과", description=rest, color=0x9933ff)
            if db.get(str(message.author.id), "gacha_mode") == "1":
                f_text = "현재 기원 : 캐릭터 픽업"
            elif db.get(str(message.author.id), "gacha_mode") == "2":
                f_text = "현재 기원 : 무기 픽업"
            else:
                f_text = "현재 기원 : 상시 기원"
            embed.set_footer(text=f_text)
            await message.channel.send(embed=embed)
        elif message.content == "!5성" or message.content == "!반천장":
            if autoreset == "1":
                m_etc.reset_stats(db, message)
            await message.channel.trigger_typing()
            rest = ""
            tries = 0
            while True:
                if tries >= 180:
                    raise ArithmeticError("루프가 허용 한도를 초과했습니다.")
                resi = m_gacha_pull.pull(db, message)
                resc = m_gacha_pull.descript_pull(resi)
                rest += str(m_gacha_pull.get_stat(db, message)[0]) + "회차 : " + resc + "\r\n"
                tries += 1
                if resi[0] == 5:
                    break
            fn = "result_" + str(int(time.time())) + "_" + str(random.randint(1000, 9999)) + ".txt"
            pf = open(fn, "w")
            pf.write(rest)
            pf.close()
            embed=discord.Embed(title=str(m_gacha_pull.get_stat(db, message)[0]) + "회차에 " + resi[2] + "이(가) 뽑혔어!", description="상세 과정은 파일을 참조해줘!", color=0xffff00)
            if db.get(str(message.author.id), "gacha_mode") == "1":
                f_text = "현재 기원 : 캐릭터 픽업"
            elif db.get(str(message.author.id), "gacha_mode") == "2":
                f_text = "현재 기원 : 무기 픽업"
            else:
                f_text = "현재 기원 : 상시 기원"
            if autoreset == "1":
                f_text += ", 자동 리셋 켜짐"
            embed.set_footer(text=f_text)
            await message.channel.send(embed=embed)
            await message.channel.send(file=discord.File(fn))
            os.remove(fn)
        elif message.content == "!천장":
            if autoreset == "1":
                m_etc.reset_stats(db, message)
            if db.get(str(message.author.id), "gacha_mode") != "3":
                await message.channel.trigger_typing()
                rest = ""
                resp = None
                resp_c = None
                tries = 0
                while True:
                    if tries >= 180:
                        raise ArithmeticError("루프가 허용 한도를 초과했습니다.")
                    resi = m_gacha_pull.pull(db, message)
                    resc = m_gacha_pull.descript_pull(resi)
                    rest += str(m_gacha_pull.get_stat(db, message)[0]) + "회차 : " + resc + "\r\n"
                    tries += 1
                    if resi[0] == 5 and resi[3]:
                        break
                    elif resi[0] == 5 and not resi[3]:
                        resp = resi
                        resp_c = str(m_gacha_pull.get_stat(db, message)[0])
                fn = "result_" + str(int(time.time())) + "_" + str(random.randint(1000, 9999)) + ".txt"
                pf = open(fn, "w")
                pf.write(rest)
                pf.close()
                embed=discord.Embed(title=str(m_gacha_pull.get_stat(db, message)[0]) + "회차에 " + resi[2] + "이(가) 뽑혔어!", description="상세 과정은 파일을 참조해줘!", color=0xffff00)
                if resp != None:
                    embed.add_field(name="비 픽업(픽뚫) 5성 항목", value="#" + resp_c + " : " + resp[2])
                if db.get(str(message.author.id), "gacha_mode") == "1":
                    f_text = "현재 기원 : 캐릭터 픽업"
                else:
                    f_text = "현재 기원 : 무기 픽업"
                if autoreset == "1":
                    f_text += ", 자동 리셋 켜짐"
                embed.set_footer(text=f_text)
                await message.channel.send(embed=embed)
                await message.channel.send(file=discord.File(fn))
                os.remove(fn)
            else:
                embed = discord.Embed(title="상시 기원에서는 '!5성' 또는 '!반천장'을 대신 사용해줘!")
                await message.channel.send(embed=embed)
        elif message.content == "!통계":
            gm = db.get(str(message.author.id), "gacha_mode")
            stat = m_gacha_pull.get_stat(db, message)
            if gm == "1":
                embed = discord.Embed(title="캐릭터 픽업 기원 통계")
            elif gm == "2":
                embed = discord.Embed(title="무기 픽업 기원 통계")
            elif gm == "3":
                embed = discord.Embed(title="상시 기원 통계")
            embed.add_field(name="뽑은 횟수", value=str(stat[0]))
            embed.add_field(name="5성 획득 횟수", value=str(stat[1]))
            embed.add_field(name="4성 획득 횟수", value=str(stat[2]))
            embed.add_field(name="3성 획득 횟수", value=str(stat[3]))
            embed.add_field(name="캐릭터 획득 횟수", value=str(stat[4]))
            embed.add_field(name="무기 획득 횟수", value=str(stat[5]))
            if gm != "3":
                embed.add_field(name="5성 일반 확률 아이템 획득(픽뚫) 횟수", value=str(stat[6]))
            await message.channel.send(embed=embed)
        elif message.content == "!리셋":
            m_etc.reset_stats(db, message)
            embed = discord.Embed(title="선택된 기원의 통계를 초기화했어!")
            await message.channel.send(embed=embed)
        elif message.content == "!자동리셋":
            if autoreset == "0":
                db.set(str(message.author.id), "autoreset", "1")
                embed = discord.Embed(title="이제 천장, 반천장 명령어를 쓰기 전에 통계를 초기화할게!")
            else:
                db.set(str(message.author.id), "autoreset", "0")
                embed = discord.Embed(title="천장, 반천장 통계 초기화를 해제했어!")
            await message.channel.send(embed=embed)
        elif message.content.startswith("!견적"):
            gm = db.get(str(message.author.id), "gacha_mode")
            cnt = int(db.get(str(message.author.id), "total_pull_" + str(gm)))
            if cnt == 0:
                embed=discord.Embed(title="먼저 시뮬레이션을 돌려서 통계를 만들어줘!")
            else:
                if message.content == "!견적":
                    embed=m_estimate.estimate(cnt)
                else:
                    m = message.content.replace("!견적 ", "")
                    try:
                        m = int(m)
                        embed=m_estimate.estimate(cnt, m)
                    except:
                        embed=discord.Embed(title="사용 방법 : !견적 (보유중인 원석 개수) / !견적")
            await message.channel.send(embed=embed)
        elif message.content.startswith("!저격"):
            if message.content == "!저격":
                embed=discord.Embed(title="사용 방법 : !저격 (항목 이름)")
                await message.channel.send(embed=embed)
            else:
                m = message.content.replace("!저격 ", "")
                if m == "클레" and not m_search.search(db, message, m):
                    embed = discord.Embed(title="클레는 나가 놀고 싶어~ 함께 밖에 나가 놀아줘~")
                    await message.channel.send(embed=embed)
                elif m_search.search(db, message, m):
                    await message.channel.trigger_typing()
                    rest = ""
                    tries = 0
                    while True:
                        if tries >= 8192:
                            raise ArithmeticError("루프가 허용 한도를 초과했습니다.")
                        tries += 1
                        resi = m_gacha_pull.pull(db, message)
                        resc = m_gacha_pull.descript_pull(resi)
                        rest += str(m_gacha_pull.get_stat(db, message)[0]) + "회차 : " + resc + "\r\n"
                        if resi[0] == 5 and resi[2] == m:
                            break
                    fn = "result_" + str(int(time.time())) + "_" + str(random.randint(1000, 9999)) + ".txt"
                    pf = open(fn, "w")
                    pf.write(rest)
                    pf.close()
                    embed=discord.Embed(title=str(m_gacha_pull.get_stat(db, message)[0]) + "회차에 " + resi[2] + "이(가) 뽑혔어!", description="상세 과정은 파일을 참조해줘!", color=0xffff00)
                    await message.channel.send(embed=embed)
                    await message.channel.send(file=discord.File(fn))
                    os.remove(fn)
                else:
                    embed = discord.Embed(title="어떤 항목이었더라? 클레는 모르겠어...")
                    await message.channel.send(embed=embed)
        elif message.content.startswith("!풀돌"):
            if message.content == "!풀돌":
                embed=discord.Embed(title="사용 방법 : !풀돌 (항목 이름)")
                await message.channel.send(embed=embed)
            else:
                m = message.content.replace("!풀돌 ", "")
                if m == "클레" and not m_search.search(db, message, m):
                    embed = discord.Embed(title="클레는 나가 놀고 싶어~ 함께 밖에 나가 놀아줘~")
                    await message.channel.send(embed=embed)
                elif m_search.search(db, message, m):
                    await message.channel.trigger_typing()
                    ix = 0
                    rest = ""
                    tries = 0
                    while True:
                        if tries >= 8192:
                            raise ArithmeticError("루프가 허용 한도를 초과했습니다.")
                        tries += 1
                        resi = m_gacha_pull.pull(db, message)
                        resc = m_gacha_pull.descript_pull(resi)
                        rest += str(m_gacha_pull.get_stat(db, message)[0]) + "회차 : " + resc + "\r\n"
                        if resi[0] == 5 and resi[2] == m:
                            ix += 1
                            if ix >= 7:
                                break
                    fn = "result_" + str(int(time.time())) + "_" + str(random.randint(1000, 9999)) + ".txt"
                    pf = open(fn, "w")
                    pf.write(rest)
                    pf.close()
                    embed=discord.Embed(title=str(m_gacha_pull.get_stat(db, message)[0]) + "회차를 끝으로 풀돌을 성공했어!", description="상세 과정은 파일을 참조해줘!", color=0xffff00)
                    await message.channel.send(embed=embed)
                    await message.channel.send(file=discord.File(fn))
                    os.remove(fn)
                else:
                    embed = discord.Embed(title="어떤 항목이었더라? 클레는 모르겠어...")
                    await message.channel.send(embed=embed)
        elif message.author.id == int(conf.get("config", "admin_id")):
            if message.content == "test_traceback":
                i = 42 / 0
            elif message.content == "get_guild_count":
                await message.channel.send(str(len(client.guilds)) + " guilds")
        else:
            return # 코드 정지, 명령어를 사용하지 않았으므로 공지사항 업로드 채널을 지정하지 않음
        try:
            db.set("announcement_channel", str(message.guild.id), str(message.channel.id))
        except:
            pass
    except Exception as e:
        if "Missing Permissions" in str(e):
            await message.channel.send('권한이 부족합니다. "링크 첨부"와 "파일 첨부" 권한을 활성화해주세요.')
        else:
            embed=discord.Embed(title="뭔가 잘못되었나 봐!", description="오류 내용 : " + str(e) + "\n클레가 오류 보고서를 전송해 놨으니까 곧 고쳐질거야!")
            await message.channel.send(embed=embed)
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

print("INFO    : connecting to Discord. Please Wait..")
client.run(conf.get("config", "bot_token"))
