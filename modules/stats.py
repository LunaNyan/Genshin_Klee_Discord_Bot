import sys, discord

import toolbox
sys.path.append("./modules/gacha_data/")
import metadata

def stacks(db, message):
    dbi = toolbox.getFromList(db, str(message.author.id), "config")
    data = metadata.get_gacha_data(dbi[0])
    # stackgroup
    if data[4] == None:
        d_stackgroup = dbi[0]
    else:
        d_stackgroup = data[4]
    # assign
    try:
        dbs = toolbox.getFromList(db, str(message.author.id), "gacha_" + d_stackgroup)
    except:
        # 손대지 않은 가챠 통계는 초기화 진행, 스탯에서는 아무것도 없는 상태로 표시됨
        toolbox.init_userdata_gacha(db, message, dbi[0])
        dbs = toolbox.getFromList(db, str(message.author.id), "gacha_" + d_stackgroup)
    return dbs[1]

def stats(db, message):
    dbi = toolbox.getFromList(db, str(message.author.id), "config")
    try:
        dbs = toolbox.getFromList(db, str(message.author.id), "gacha_" + dbi[0])
    except:
        # 손대지 않은 가챠 통계는 초기화 진행, 스탯에서는 아무것도 없는 상태로 표시됨
        toolbox.init_userdata_gacha(db, message, dbi[0])
        dbs = toolbox.getFromList(db, str(message.author.id), "gacha_" + dbi[0])
    embed=discord.Embed(title="기원 통계 : " + metadata.get_gacha_name(dbi[0]))
    embed.add_field(name="총 기원 횟수", value=dbs[0])
    embed.add_field(name="5★ 천장", value=dbs[1])
    embed.add_field(name="4★ 천장", value=dbs[2])
    embed.add_field(name="캐릭터 획득 횟수", value=dbs[5])
    embed.add_field(name="무기 획득 횟수", value=dbs[6])
    if dbi[0] == "S0100":
        embed.add_field(name="5성 캐릭터 획득 횟수", value=dbs[8])
        embed.add_field(name="5성 무기 획득 횟수", value=dbs[7])
        embed.add_field(name="4성 아이템 획득 횟수", value=dbs[9])
    else:
        embed.add_field(name="5성 아이템 획득 횟수", value=dbs[8])
        embed.add_field(name="4성 아이템 획득 횟수", value=dbs[9])
        embed.add_field(name="5성 비 픽업 아이템 획득(픽뚫) 횟수", value=dbs[7])
    embed.set_footer(text="통계 초기화 : !리셋")
    return embed

def reset(db, message):
    dbi = toolbox.getFromList(db, str(message.author.id), "config")
    toolbox.init_userdata_gacha(db, message, dbi[0])
    embed=discord.Embed(title=metadata.get_gacha_name(dbi[0]) + "의 기원 통계를 초기화했어!")
    return embed

def set_stack(db, message):
    dbi = toolbox.getFromList(db, str(message.author.id), "config")
    if message.content == "!스택":
        embed = discord.Embed(title="사용 방법 : !스택 (개수)[#]")
        embed.set_footer(text="현재 선택된 기원 : " + metadata.get_gacha_name(dbi[0]) + ", 숫자 뒤에 '#'을 붙이면 반천장 픽뚫 상태를 마킹합니다")
    else:
        m = message.content.replace("!스택 ", "")
        try:
            if "#" in m:
                mx = m.replace("#", "")
            else:
                mx = m
            if int(mx) <= 0 or int(mx) >= 90:
                embed = discord.Embed(title="1 ~ 89 사이의 숫자를 입력해줘!")
                return embed
        except:
            embed = discord.Embed(title="예시 : !스택 74")
            embed.set_footer(text="숫자 뒤에 '#'을 붙이면 반천장 픽뚫 상태를 마킹합니다")
            return embed
        dbs = toolbox.getFromList(db, str(message.author.id), "gacha_" + dbi[0])
        if "#" in m:
            m = m.replace("#", "")
            dbs[3] = "1"
        dbs[1] = str(m)
        dbs[2] = str(m)[-1:]
        toolbox.setToList(db, str(message.author.id), "gacha_" + dbi[0], dbs)
        embed = discord.Embed(title="스택을 설정했어!")
    return embed

def estimate(cnt, gems_preowned=0):
    gems = cnt * 160 # 필요한 원석 수 계산
    gems -= gems_preowned # 이미 갖고 있는 원석 수가 기입된 경우 추가
    crystals = 0 # 필요한 창세의 결정 수
    crs_0 = 0 # 창세의 결정 60개(1200원) 결제 수량
    crs_1 = 0 # 창세의 결정 330개(300+30개, 5900원) 결제 수량
    crs_2 = 0 # 창세의 결정 1090개(980+110개, 19000원) 결제 수량
    crs_3 = 0 # 창세의 결정 2240개(1980+260개, 37000원) 결제 수량
    crs_4 = 0 # 창세의 결정 3880개(3280+600개, 65000원) 결제 수량
    crs_5 = 0 # 창세의 결정 8080개(6480+1600개, 119000원) 결제 수량
    #결정 8080개
    while True:
        gems -= 8080
        if gems < -4000:
            gems += 8080
            break
        else:
            crs_5 += 1
            crystals += 8080
            continue
    # 결정 3880개
    while True:
        gems -= 3880
        if gems < -2700:
            gems += 3880
            break
        else:
            crs_4 += 1
            crystals += 3880
            continue
    # 결정 2240개
    while True:
        gems -= 2240
        if gems < -1800:
            gems += 2240
            break
        else:
            crs_3 += 1
            crystals += 2240
            continue
    # 결정 1090개
    while True:
        gems -= 1090
        if gems < -800:
            gems += 1090
            break
        else:
            crs_2 += 1
            crystals += 1090
            continue
    # 결정 330개
    while True:
        gems -= 330
        if gems < -300:
            gems += 330
            break
        else:
            crs_1 += 1
            crystals += 330
            continue
    # 결정 60개
    while True:
        gems -= 60
        if gems < 0:
            break
        else:
            continue
        crs_0 += 1
        crystals += 60
    # 결정 당 금액 계산
    crm_0 = crs_0 * 1200 # 창세의 결정 60개(1200원)
    crm_1 = crs_1 * 5900 # 창세의 결정 330개(300+30개, 5900원)
    crm_2 = crs_2 * 19000 # 창세의 결정 1090개(980+110개, 19000원)
    crm_3 = crs_3 * 37000 # 창세의 결정 2240개(1980+260개, 37000원)
    crm_4 = crs_4 * 65000 # 창세의 결정 3880개(3280+600개, 65000원)
    crm_5 = crs_5 * 119000 # 창세의 결정 8080개(6480+1600개, 119000원)
    if crystals + gems < 0:
        req_gems = 0
    else:
        req_gems = crystals + gems
    # discord embed 처리
    embed = discord.Embed(title="견적서를 뽑아왔어!")
    embed.add_field(name="기원 횟수", value=str(cnt), inline=True)
    embed.add_field(name="필요한 창세의 결정 수", value=str(req_gems), inline=True)
    text = "```창세의 결정 8080개(6480+1600개, 119000원) : " + str(crs_5) + "개 (" + str(crm_5) + "원)\n"
    text+= "창세의 결정 3880개(3280+600개, 65000원) : " + str(crs_4) + "개 (" + str(crm_4) + "원)\n"
    text+= "창세의 결정 2240개(1980+260개, 37000원) : " + str(crs_3) + "개 (" + str(crm_3) + "원)\n"
    text+= "창세의 결정 1090개(980+110개, 19000원) : " + str(crs_2) + "개 (" + str(crm_2) + "원)\n"
    text+= "창세의 결정 330개(300+30개, 5900원) : " + str(crs_1) + "개 (" + str(crm_1) + "원)\n"
    text+= "창세의 결정 60개(1200원) : " + str(crs_0) + "개 (" + str(crm_0) + "원)```"
    embed.add_field(name="상세 정보", value=text, inline=False)
    embed.add_field(name="총 소모 금액", value="**" + toolbox.groupNum(crm_0 + crm_1 + crm_2 + crm_3 + crm_4 + crm_5) + "원**", inline=True)
    embed.add_field(name="구매한 창세의 결정 수", value=str(crystals), inline=True)
    embed.add_field(name="잉여 원석 / 결정 수", value=str(gems)[1:] + "개", inline=True)
    return embed
