import sys, discord, math

import toolbox
sys.path.append("./modules/gacha_data/")
import metadata

def gacha_list(db, message):
    li = metadata.get_gachas()
    dbi = toolbox.getFromList(db, str(message.author.id), "config")
    embed=discord.Embed(title="현재 선택된 기원 : " + metadata.get_gacha_name(dbi[0]), description="기원 선택 방법 : !기원 (번호)")
    for l in li:
        if metadata.current_char_sub != None and l[0] == metadata.current_char_sub: # 이중픽업
            embed.add_field(name="#0 : " + l[1][0], value="기원 기간 : " + l[1][2] + ", 버전 : " + l[1][1], inline=False)
        if l[0] == metadata.current_char:
            embed.add_field(name="#1 : " + l[1][0], value="기원 기간 : " + l[1][2] + ", 버전 : " + l[1][1], inline=False)
        if l[0] == metadata.current_weapon:
            embed.add_field(name="#2 : " + l[1][0], value="기원 기간 : " + l[1][2] + ", 버전 : " + l[1][1], inline=False)
        if l[0] == metadata.current_standard:
            embed.add_field(name="#3 : " + l[1][0], value="기원 기간 : " + l[1][2] + ", 버전 : " + l[1][1], inline=False)
    embed.set_footer(text="더 많은 기원 목록을 보려면 : !목록")
    return embed

def gacha_list_detailed(message):
    li = metadata.get_gachas()
    nm = 0
    for l in li:
        if metadata.current_char_sub != None and l[0] == metadata.current_char_sub:
            del(li[nm])
        elif l[0] == metadata.current_standard:
            del(li[nm])
        elif l[0] == metadata.current_char:
            del(li[nm])
        elif l[0] == metadata.current_weapon:
            del(li[nm])
        nm += 1
    pages = math.ceil(len(li) / 5)
    try:
        m = message.content.replace("!목록 ", "")
        if int(m) <= 0:
            page = 1
        elif int(m) >= pages:
            page = pages
        else:
            page = int(m)
    except:
        page = 1
    c = (page - 1) * 5
    liw = li[c:c+5]
    embed=discord.Embed(title="기원 목록 (총 " + str(len(li)) + "개)", color=0xffffff)
    nx = 10 + ((page - 1) * 5)
    for w in liw:
        embed.add_field(name="#" + str(nx) + " : " + w[1][0], value="기원 기간 : " + w[1][2] + ", 버전 : " + w[1][1], inline=False)
        nx += 1
    embed.set_footer(text=str(page) + ' / ' + str(pages) + ' 페이지, 다른 페이지 보기 : !목록 (페이지)')
    return embed

def select_gacha(db, message):
    m = message.content.replace("!기원 ", "")
    c = toolbox.getFromList(db, str(message.author.id), "config")
    li = metadata.get_gachas()
    nm = 0
    for l in li:
        if metadata.current_char_sub != None and l[0] == metadata.current_char_sub:
            del(li[nm])
        elif l[0] == metadata.current_char:
            del(li[nm])
        elif l[0] == metadata.current_weapon:
            del(li[nm])
        elif l[0] == metadata.current_standard:
            del(li[nm])
        nm += 1
    if m == "3":
        c[0] = metadata.current_standard
        res = "상시 기원"
    elif m == "1":
        c[0] = metadata.current_char
        res = "현재 캐릭터 픽업 기원"
    elif m == "2":
        c[0] = metadata.current_weapon
        res = "현재 무기 기원"
    elif metadata.current_char_sub != None and m == "0":
        c[0] = metadata.current_char_sub
        res = "현재 부 캐릭터 픽업 기원"
    else:
        try:
            nm = int(m) - 10
            c[0] = li[nm][0]
            res = li[nm][1][0]
        except:
            raise ValueError
    toolbox.setToList(db, str(message.author.id), "config", c)
    return res

def select_gacha_intl(db, message, idx):
    c = toolbox.getFromList(db, str(message.author.id), "config")
    c[0] = idx
    toolbox.setToList(db, str(message.author.id), "config", c)

def gacha_info(db, message):
    dbi = toolbox.getFromList(db, str(message.author.id), "config")
    da = metadata.get_gacha_data(dbi[0])
    embed = discord.Embed(title="기원 정보 : " + da[1][0])
    if dbi[0] != "S0100":
        pc5 = ""
        for i in da[2][0][0]:
            pc5 += i[2] + ", "
        embed.add_field(name="픽업 5성 아이템", value=pc5[:-2])
        pc4 = ""
        for i in da[2][1][0]:
            pc4 += i[2] + ", "
        embed.add_field(name="픽업 4성 아이템", value=pc4[:-2])
    embed.add_field(name="기원 기간", value=da[1][2], inline=False)
    embed.add_field(name="데이터베이스 버전", value=da[1][1])
    embed.set_image(url="https://neonmonsters.kro.kr/idc/genshin/banner/" + dbi[0] + ".jpg")
    return embed