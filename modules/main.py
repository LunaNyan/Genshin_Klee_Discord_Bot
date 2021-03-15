import sys, os, discord, configparser, logging
import m_gacha_pull, m_help
sys.path.append('../gacha_data/')
import pickup_character, pickup_weapon, anytime
sys.path.append('../')

bot_ver = "0.10"

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
    if message.author == client.user:
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
    if message.content == "!도움":
        await message.channel.send(embed=m_help.help(bot_ver))
    elif message.content.startswith("!기원"):
        if message.content == "!기원":
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
            rest += str(m_gacha_pull.get_stat(db, message)[0]) + "회차 : " + resc + "\n"
        if encountered_5star:
            embed = discord.Embed(title="10연차 결과", description=rest, color=0xffff00)
        else:
            embed = discord.Embed(title="10연차 결과", description=rest, color=0x9933ff)
        await message.channel.send(embed=embed)
    elif message.content == "!5성" or message.content == "!반천장":
        await message.channel.trigger_typing()
        rest = ""
        while True:
            resi = m_gacha_pull.pull(db, message)
            resc = m_gacha_pull.descript_pull(resi)
            rest += str(m_gacha_pull.get_stat(db, message)[0]) + "회차 : " + resc + "\n"
            if resi[0] == 5:
                break
        pf = open("result.txt", "w")
        pf.write(rest)
        pf.close()
        embed=discord.Embed(title=str(m_gacha_pull.get_stat(db, message)[0]) + "회차에 " + resi[2] + "이(가) 뽑혔어!", description="상세 과정은 파일을 참조해줘!", color=0xffff00)
        await message.channel.send(embed=embed)
        await message.channel.send(file=discord.File("result.txt"))
        os.remove("result.txt")
    elif message.content == "!천장":
        await message.channel.trigger_typing()
        rest = ""
        while True:
            resi = m_gacha_pull.pull(db, message)
            resc = m_gacha_pull.descript_pull(resi)
            rest += str(m_gacha_pull.get_stat(db, message)[0]) + "회차 : " + resc + "\n"
            if db.get(str(message.author.id), "gacha_mode") != "3":
                if resi[0] == 5 and resi[3]:
                    break
            else:
                if resi[0] == 5 and resi[1] == 'character':
                    break
        pf = open("result.txt", "w")
        pf.write(rest)
        pf.close()
        embed=discord.Embed(title=str(m_gacha_pull.get_stat(db, message)[0]) + "회차에 " + resi[2] + "이(가) 뽑혔어!", description="상세 과정은 파일을 참조해줘!", color=0xffff00)
        await message.channel.send(embed=embed)
        await message.channel.send(file=discord.File("result.txt"))
        os.remove("result.txt")
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
        gm = int(db.get(str(message.author.id), "gacha_mode"))
        db.set(str(message.author.id), "stack_5star_pull_" + str(gm), "0")
        db.set(str(message.author.id), "stack_4star_pull_" + str(gm), "0")
        if gm != 3:
            db.set(str(message.author.id), "stack_5star_nothope_" + str(gm), "0")
            db.set(str(message.author.id), "stack_4star_nothope_" + str(gm), "0")
            db.set(str(message.author.id), "total_nothope_" + str(gm), "0")
        db.set(str(message.author.id), "total_pull_" + str(gm), "0")
        db.set(str(message.author.id), "total_5star_" + str(gm), "0")
        db.set(str(message.author.id), "total_4star_" + str(gm), "0")
        db.set(str(message.author.id), "total_3star_" + str(gm), "0")
        db.set(str(message.author.id), "total_character_" + str(gm), "0")
        db.set(str(message.author.id), "total_item_" + str(gm), "0")
        embed = discord.Embed(title="선택된 기원의 통계를 초기화했어!")
        await message.channel.send(embed=embed)
    with open(db_path, 'w') as configfile:
        db.write(configfile)

print("INFO    : connecting to Discord. Please Wait..")
client.run(conf.get("config", "bot_token"))