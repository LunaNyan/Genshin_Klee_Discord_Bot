import sys, discord, datetime, json, base64, time, random, math

sys.path.append("./modules/gacha_data/")
import metadata

def checkTrait(text, mode=False):
    c = text[-1:]
    if int((ord(c) - 0xAC00) % 28) != 0:
        if mode:
            return "을"
        else:
            return "이"
    else:
        if mode:
            return "를"
        else:
            return "가"

def dailyresin():
    d = datetime.date.today()
    d = d.isoweekday()
    embed = discord.Embed(title="금일 파밍 가능한 육성 재료")
    if d == 1 or d == 4:
        embed.add_field(name="몬드 지역 특성 재료", value="자유 (디오나, 바바라, 설탕, 엠버, 클레, 타르탈리아, 에일로이)")
        embed.add_field(name="리월 지역 특성 재료", value="번영 (각청, 로자리아, 소, 응광, 치치)")
        embed.add_field(name="이나즈마 지역 특성 재료", value="부세 (요이미야, 산고노미야 코코미, 토마)")
        embed.add_field(name="무기 돌파 재료", value="고탑 왕, 고운한림, 먼바다의 산호")
    elif d == 2 or d == 5:
        embed.add_field(name="몬드 지역 특성 재료", value="투쟁 (노엘, 다이루크, 레이저, 모나, 베넷, 유라)")
        embed.add_field(name="리월 지역 특성 재료", value="근면 (감우, 중운, 향릉, 호두, 카에데하라 카즈하)")
        embed.add_field(name="이나즈마 지역 특성 재료", value="풍아 (카미사토 아야카, 쿠죠 사라, 아라타키 이토)")
        embed.add_field(name="무기 돌파 재료", value="칼바람 울프, 안개구름, 나루카미 어령")
    elif d == 3 or d == 6:
        embed.add_field(name="몬드 지역 특성 재료", value="시문 (리사, 벤티, 알베도, 케이아, 피슬)")
        embed.add_field(name="리월 지역 특성 재료", value="황금 (북두, 신염, 연비, 종려, 행추)")
        embed.add_field(name="이나즈마 지역 특성 재료", value="천광 (사유, 라이덴 쇼군, 고로)")
        embed.add_field(name="무기 돌파 재료", value="라이언 투사, 흑운철, 금석극화")
    elif d == 7:
        embed.add_field(name="몬드 지역 특성 재료", value="모든 캐릭터 가능")
        embed.add_field(name="리월 지역 특성 재료", value="모든 캐릭터 가능")
        embed.add_field(name="이나즈마 지역 특성 재료", value="모든 캐릭터 가능")
        embed.add_field(name="무기 돌파 재료", value="모든 재료 가능")
    return embed

def getOnce(db, section, key):
    i = str(base64.b64decode(db.get(section, key)).decode('utf-8'))
    return i

def setOnce(db, section, key, value):
    e = base64.b64encode(value.encode('utf-8'))
    e = str(e).replace("b'", "")
    e = e.replace("'", "")
    db.set(section, key, e)

def getFromList(db, section, key, seperator=","):
    i = str(base64.b64decode(db.get(section, key)).decode('utf-8'))
    il = i.split(seperator)
    return il

def setToList(db, section, key, value, seperator=","):
    t = ""
    for i in value:
        t += i + seperator
    t = t[:-1]
    e = base64.b64encode(t.encode('utf-8'))
    e = str(e).replace("b'", "")
    e = e.replace("'", "")
    db.set(section, key, e)

def getFromJson(db, section, key):
    i = str(base64.b64decode(db.get(section, key)).decode('utf-8'))
    ij = json.loads(i)
    return ij

def setToJson(db, section, key, dic):
    ij = json.dumps(dic)
    e = base64.b64encode(ij.encode('utf-8'))
    e = str(e).replace("b'", "")
    e = e.replace("'", "")
    db.set(section, key, e)

def groupNum(number):
    s = '%d' % number
    groups = []
    while s and s[-1].isdigit():
        groups.append(s[-3:])
        s = s[:-3]
    return s + ','.join(reversed(groups))

def preetify(res, mode=False):
    stars = ""
    typ = ""
    if res[0] == 3:
        stars = "★★★☆☆"
    elif res[0] == 4:
        stars = "★★★★☆"
    elif res[0] == 5:
        stars = "★★★★★"
    if res[1] == "character":
        typ = "캐릭터"
    elif res[1] == "item":
        typ = "무기"
    if mode and res[0] == 5:
        return "**" + stars + " " + typ + " : " + str(res[2]) + "**"
    else:
        return stars + " " + typ + " : " + str(res[2])

def init_userdata_config(db, message):
    # userdata desc
    # 현재 기원, 자동리셋 사용 여부, txt 파일에 3성 포함 여부, 12시간제 사용 여부
    setToList(db, str(message.author.id), "config", [metadata.current_standard, "0", "0", "0"])

def init_userdata_gacha(db, message, keyid):
    setToList(db, str(message.author.id), "gacha_" + keyid, ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0"])

def saveToFile(db, message, res):
    append3star = False
    dbi = getFromList(db, str(message.author.id), "config")
    try:
        if dbi[2] == "1":
            append3star = True
        else:
            append3star = False
    except:
        dbi.append("0")
        setToList(db, str(message.author.id), "config", dbi)
    tries = res[4] - res[3] + 1
    rest = ""
    seperator = 0
    for r in res[1]:
        if append3star == False and r[0] != 3:
            rest += str(tries) + "회차 : " + preetify(r) + "\r\n"
            seperator += 1
        elif append3star:
            rest += str(tries) + "회차 : " + preetify(r) + "\r\n"
            seperator += 1
        if seperator == 9:
            rest += "\r\n"
            seperator = 0
        tries += 1
    fn = "result_" + str(int(time.time())) + "_" + str(random.randint(1000, 9999)) + ".txt"
    pf = open(fn, "w")
    pf.write(rest)
    pf.close()
    return fn

def parseTime(seconds):
    hours = math.trunc(seconds / 3600)
    seconds -= (hours * 3600)
    minutes = math.trunc(seconds / 60)
    seconds -= (minutes * 60)
    return [hours, minutes, seconds]

def time24to12(dt):
    # create time to int
    dh = int(dt.strftime("%H"))
    dm = int(dt.strftime("%M"))
    # hours
    if dh == 0:
        dhh = "오전 12시"
    elif dh == 12:
        dhh = "오후 12시"
    elif dh >= 13:
        dhh = dh - 12
        if dhh <= 9:
            dhh = "오후 0" + str(dhh) + "시"
        else:
            dhh = "오후 " + str(dhh) + "시"
    elif dh <= 9:
        dhh = "오전 0" + str(dh) + "시"
    else:
        dhh = "오전 " + str(dh) + "시"
    # minutes
    if dm <= 9:
        dmm = "0" + str(dm) + "분"
    else:
        dmm = str(dm) + "분"
    return dhh + " " + dmm

def resin(amount, message, db):
    if amount > 160 or amount < 0:
        embed=discord.Embed(title="레진 잔량은 0보다 아래거나 160을 초과할 수 없어!")
    elif amount == 160:
        embed=discord.Embed(title="레진이 풀 충전 상태야! 빨리 써줘!")
    else:
        # 남은 시간
        amx = (160 - amount) * 8  * 60
        tc = parseTime(amx)
        # 예상 완료 시각
        dt = datetime.datetime.now() + datetime.timedelta(seconds=amx)
        # 12시간제 사용 여부 확인
        dbi = getFromList(db, str(message.author.id), "config")
        try:
            if dbi[3] == "0":
                dtt = dt.strftime("%H") + "시 " + dt.strftime("%M") + "분"
            else:
                dtt = time24to12(dt)
        except:
            dbi.append("0")
            dtt = dt.strftime("%H:%M")
        if datetime.datetime.now().strftime("%d") != dt.strftime("%d"):
            t0 = "익일 " + dtt
        else:
            t0 = "금일 " + dtt
        embed=discord.Embed(title="레진 풀 충전까지 " + str(tc[0]) + "시간 " + str(tc[1]) + "분 남았어!", description="예상 충전 완료 시각 : " + t0)
    return embed