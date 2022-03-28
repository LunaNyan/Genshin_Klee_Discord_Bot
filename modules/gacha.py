import sys, secrets, random

import toolbox
sys.path.append("./modules/gacha_data/")
import metadata

def generate_random():
    # 크립토랜덤 실수 생성
    t = secrets.token_bytes(4)
    t2 = int.from_bytes(t, byteorder='little', signed=False)
    return t2 / 4294967295

def calc_gacha(data, pity_5s, pity_4s, s5s5050, s4s5050, total_char, total_item, total_nh5, total_5s, total_4s, d_prob, is_standard=False):
    # 가챠 스펙트럼 생성
    if pity_5s >= d_prob[4]: # 5성 확률 보정
        h_5s = 1 - d_prob[5]
    else: # 5성 일반 확률
        h_5s = 1 - d_prob[2]
    if pity_4s >= d_prob[6]:
        h_4s = h_5s - d_prob[7]
    else:
        h_4s = h_5s - d_prob[3]
    nh50 = None
    # 랜덤 생성
    s = generate_random()
    random.seed(generate_random())
    # 가챠 진행 (상시)
    if is_standard:
        # 5성 출현
        if s >= h_5s or pity_5s >= d_prob[8]:
            # 픽업 or 픽뚫
            if (s5s5050 == "1" and generate_random() >= 0.25) or generate_random() >= 0.5:
                result = random.choice(data[0][0])
                s5s5050 = "0"
                total_5s += 1
                if result[1] == "character":
                    total_char += 1
                else:
                    total_item += 1
            else:
                result = random.choice(data[0][1])
                nh50 = result
                s5s5050 = "1"
                total_5s += 1
                total_nh5 += 1
                if result[1] == "character":
                    total_char += 1
                else:
                    total_item += 1
            pity_5s = 0
        # 4성 출현
        elif s >= h_4s or pity_4s >= d_prob[9]:
            # 픽업 or 픽뚫
            if (s4s5050 == "1" and generate_random() >= 0.25) or generate_random() >= 0.5:
                result = random.choice(data[1][0])
                s4s5050 = "0"
            else:
                result = random.choice(data[1][1])
                s4s5050 = "1"
            pity_4s = 0
            pity_5s += 1
            total_4s += 1
            if result[1] == "character":
                total_char += 1
            else:
                total_item += 1
        # 3성 출현
        else:
            result = random.choice(metadata.get_3stars())
            pity_4s += 1
            pity_5s += 1
            total_item += 1
    # 가챠 진행 (비 상시)
    else:
        # 5성 출현
        if s >= h_5s or pity_5s >= d_prob[8]:
            # 픽업 or 픽뚫
            if s5s5050 == "1" or generate_random() >= d_prob[0]:
                result = random.choice(data[0][0])
                s5s5050 = "0"
                total_5s += 1
                if result[1] == "character":
                    total_char += 1
                else:
                    total_item += 1
            else:
                result = random.choice(data[0][1])
                nh50 = result
                s5s5050 = "1"
                total_5s += 1
                total_nh5 += 1
                if result[1] == "character":
                    total_char += 1
                else:
                    total_item += 1
            pity_5s = 0
        # 4성 출현
        elif s >= h_4s or pity_4s >= d_prob[9]:
            # 픽업 or 픽뚫
            if s4s5050 == "1" or generate_random() >= d_prob[1]:
                result = random.choice(data[1][0])
                s4s5050 = "0"
            else:
                result = random.choice(data[1][1])
                s4s5050 = "1"
            pity_4s = 0
            pity_5s += 1
            total_4s += 1
            if result[1] == "character":
                total_char += 1
            else:
                total_item += 1
        # 3성 출현
        else:
            result = random.choice(metadata.get_3stars())
            pity_4s += 1
            pity_5s += 1
            total_item += 1
    return [result, pity_5s, pity_4s, s5s5050, s4s5050, total_char, total_item, total_nh5, total_5s, total_4s, nh50]

def do_gacha(db, message, amount=1, snipeFor=None, mode=0, c_amounts=1):
    # mode == 1 : 천장
    # mode == 2 : 반천장
    dbi = toolbox.getFromList(db, str(message.author.id), "config")
    data = metadata.get_gacha_data(dbi[0])
    if dbi[0].startswith("S"):
        is_standard = True
    else:
        is_standard = False
    # 가챠 데이터 가져오기
    d_meta = data[1]
    d_wishlists = data[2]
    d_prob = data[3]
    if data[4] == None:
        d_stackgroup = dbi[0]
    else:
        d_stackgroup = data[4]
    try:
        dbs = toolbox.getFromList(db, str(message.author.id), "gacha_" + d_stackgroup)
    except:
        toolbox.init_userdata_gacha(db, message, d_stackgroup)
        dbs = toolbox.getFromList(db, str(message.author.id), "gacha_" + d_stackgroup)
    # 유저 가챠 스탯 가져오기
    total_amount = int(dbs[0])
    pity_5s = int(dbs[1])
    pity_4s = int(dbs[2])
    s5s5050 = int(dbs[3])
    s4s5050 = int(dbs[4])
    total_char = int(dbs[5])
    total_item = int(dbs[6])
    total_nh5 = int(dbs[7])
    total_5s = int(dbs[8])
    total_4s = int(dbs[9])
    nh50 = None
    nh50tr = None
    # 회차수 변수
    turns = 0
    turns_nh = 0
    # 가챠 결과 저장용 트럭 생성
    res_truck = []
    # 가챠 진행
    if amount >= 2:
        # n연차 진행
        for _ in range(amount):
            res = calc_gacha(d_wishlists, pity_5s, pity_4s, s5s5050, s4s5050, total_char, total_item, total_nh5, total_5s, total_4s, d_prob, is_standard)
            total_amount += 1
            pity_5s = res[1]
            pity_4s = res[2]
            s5s5050 = res[3]
            s4s5050 = res[4]
            total_char = res[5]
            total_item = res[6]
            total_nh5 = res[7]
            total_5s = res[8]
            total_4s = res[9]
            if res[10] != None:
                nh50 = res[10]
                nh50tr = [total_amount, turns + 1]
            res_truck.append(res[0])
            turns += 1
            if nh50 != None:
                turns_nh += 1
    elif snipeFor != None:
        # 저격 진행 전 이름 검색
        names = []
        for n in d_wishlists[0][0]:
            names.append(n[2])
        for n in d_wishlists[0][1]:
            names.append(n[2])
        for n in d_wishlists[1][0]:
            names.append(n[2])
        for n in d_wishlists[1][1]:
            names.append(n[2])
        if snipeFor not in names:
            # 찾는 저격 대상이 없는 경우 에러
            raise NameError
        # 저격 진행
        while True:
            while True:
                res = calc_gacha(d_wishlists, pity_5s, pity_4s, s5s5050, s4s5050, total_char, total_item, total_nh5, total_5s, total_4s, d_prob, is_standard)
                total_amount += 1
                pity_5s = res[1]
                pity_4s = res[2]
                s5s5050 = res[3]
                s4s5050 = res[4]
                total_char = res[5]
                total_item = res[6]
                total_nh5 = res[7]
                total_5s = res[8]
                total_4s = res[9]
                if res[10] != None:
                    nh50 = res[10]
                    nh50tr = [total_amount, turns + 1]
                res_truck.append(res[0])
                turns += 1
                if nh50 != None:
                    turns_nh += 1
                if res[0][2] == snipeFor:
                    break
                else:
                    continue
            c_amounts -= 1
            if c_amounts == 0:
                break
            else:
                continue
    elif mode != 0:
        names = []
        if mode == 1:
            for n in d_wishlists[0][0]:
                names.append(n[2])
        if mode == 2:
            for n in d_wishlists[0][1]:
                names.append(n[2])
        while True:
            res = calc_gacha(d_wishlists, pity_5s, pity_4s, s5s5050, s4s5050, total_char, total_item, total_nh5, total_5s, total_4s, d_prob, is_standard)
            total_amount += 1
            pity_5s = res[1]
            pity_4s = res[2]
            s5s5050 = res[3]
            s4s5050 = res[4]
            total_char = res[5]
            total_item = res[6]
            total_nh5 = res[7]
            total_5s = res[8]
            total_4s = res[9]
            if res[10] != None:
                nh50 = res[10]
                nh50tr = [total_amount, turns + 1]
            res_truck.append(res[0])
            turns += 1
            if nh50 != None:
                turns_nh += 1
            if res[0][2] in names:
                break
            else:
                continue
    else:
        # 단차
        res = calc_gacha(d_wishlists, pity_5s, pity_4s, s5s5050, s4s5050, total_char, total_item, total_nh5, total_5s, total_4s, d_prob, is_standard)
        res_truck.append(res[0])
        total_amount += 1
        pity_5s = res[1]
        pity_4s = res[2]
        s5s5050 = res[3]
        s4s5050 = res[4]
        total_char = res[5]
        total_item = res[6]
        total_nh5 = res[7]
        total_5s = res[8]
        total_4s = res[9]
        if res[10] != None:
            nh50 = res[10]
            nh50tr = [total_amount, turns + 1]
        turns += 1
        if nh50 != None:
            turns_nh += 1
    # 데이터 저장 및 결과 출력
    li = [
            str(total_amount), str(pity_5s), str(pity_4s),
            str(s5s5050), str(s4s5050),
            str(total_char), str(total_item),
            str(total_nh5), str(total_5s), str(total_4s)
         ]
    toolbox.setToList(db, str(message.author.id), "gacha_" + d_stackgroup, li)
    return [d_meta, res_truck, li, turns, total_amount, nh50, nh50tr, turns_nh]