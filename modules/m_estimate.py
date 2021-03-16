import sys, discord

if __name__=="__main__":
    print("FATAL   : Run this bot from right way.")
    sys.exit(1)

def group(number):
    s = '%d' % number
    groups = []
    while s and s[-1].isdigit():
        groups.append(s[-3:])
        s = s[:-3]
    return s + ','.join(reversed(groups))

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
    # discord embed 처리
    embed = discord.Embed(title="견적서를 뽑아왔어!")
    embed.add_field(name="기원 횟수", value=str(cnt), inline=True)
    embed.add_field(name="필요한 창세의 결정 수", value=str(crystals + gems), inline=True)
    text = "```창세의 결정 8080개(6480+1600개, 119000원) : " + str(crs_5) + "개 (" + str(crm_5) + "원)\n"
    text+= "창세의 결정 3880개(3280+600개, 65000원) : " + str(crs_4) + "개 (" + str(crm_4) + "원)\n"
    text+= "창세의 결정 2240개(1980+260개, 37000원) : " + str(crs_3) + "개 (" + str(crm_3) + "원)\n"
    text+= "창세의 결정 1090개(980+110개, 19000원) : " + str(crs_2) + "개 (" + str(crm_2) + "원)\n"
    text+= "창세의 결정 330개(300+30개, 5900원) : " + str(crs_1) + "개 (" + str(crm_1) + "원)\n"
    text+= "창세의 결정 60개(1200원) : " + str(crs_0) + "개 (" + str(crm_0) + "원)```"
    embed.add_field(name="상세 정보", value=text, inline=False)
    embed.add_field(name="총 소모 금액", value="**" + group(crm_0 + crm_1 + crm_2 + crm_3 + crm_4 + crm_5) + "원**", inline=True)
    embed.add_field(name="구매한 창세의 결정 수", value=str(crystals), inline=True)
    embed.add_field(name="잉여 원석 / 결정 수", value=str(gems)[1:] + "개", inline=True)
    return embed