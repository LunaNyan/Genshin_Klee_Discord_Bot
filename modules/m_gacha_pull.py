import sys

if __name__=="__main__":
    print("FATAL   : Run this bot from right way.")
    sys.exit(1)

import discord, secrets, random
sys.path.append('../gacha_data/')
import pickup_character, pickup_weapon, anytime
sys.path.append('../')

def generate_random():
    # 크립토랜덤 실수 생성
    t = secrets.token_bytes(4)
    t2 = int.from_bytes(t, byteorder='little', signed=False)
    return t2 / 4294967295

def get_gacha_mode(db, message):
    # 유저가 선택한 가챠 모드를 가져옴
    # 1 : 캐릭터 픽업
    # 2 : 무기 픽업
    # 3 : 상시
    gm = int(db.get(str(message.author.id), "gacha_mode"))
    if gm == 1: # 캐릭터 픽업 기원
        return [
                False, # 상시 기원 여부
                [pickup_character.l_5star_up, pickup_character.l_5star_std], # 5성 확률UP 항목, 5성 일반 확률 항목
                [pickup_character.l_4star_up, pickup_character.l_4star_std], # 4성 확률UP 항목, 4성 일반 확률 항목
                pickup_character.l_3star_std, # 3성 일반 확률 항목
                [pickup_character.huddle_5star_up, pickup_character.huddle_5star], # 5성 확률UP 확률, 5성 일반 확률
                [pickup_character.huddle_4star_up, pickup_character.huddle_4star], # 4성 확률UP 확률, 4성 일반 확률
                [pickup_character.huddle_stack_5star, pickup_character.huddle_stack_5star_up], # 5성 확률 보정이 시작되는 스택 수, 보정되는 5성 확률
                [pickup_character.huddle_stack_4star, pickup_character.huddle_stack_4star_up], # 4성 확률 보정이 시작되는 스택 수, 보정되는 4성 확률
                [pickup_character.ceiling_5star, pickup_character.ceiling_4star] # 5성 천장, 4성 천장
               ]
    elif gm == 2: # 무기 픽업 기원
        return [
                False, # 상시 기원 여부
                [pickup_weapon.l_5star_up, pickup_weapon.l_5star_std], # 5성 확률UP 항목, 5성 일반 확률 항목
                [pickup_weapon.l_4star_up, pickup_weapon.l_4star_std], # 4성 확률UP 항목, 4성 일반 확률 항목
                pickup_weapon.l_3star_std, # 3성 일반 확률 항목
                [pickup_weapon.huddle_5star_up, pickup_weapon.huddle_5star], # 5성 확률UP 확률, 5성 일반 확률
                [pickup_weapon.huddle_4star_up, pickup_weapon.huddle_4star], # 4성 확률UP 확률, 4성 일반 확률
                [pickup_weapon.huddle_stack_5star, pickup_weapon.huddle_stack_5star_up], # 5성 확률 보정이 시작되는 스택 수, 보정되는 5성 확률
                [pickup_weapon.huddle_stack_4star, pickup_weapon.huddle_stack_4star_up], # 4성 확률 보정이 시작되는 스택 수, 보정되는 4성 확률
                [pickup_weapon.ceiling_5star, pickup_weapon.ceiling_4star] # 5성 천장, 4성 천장
               ]
    elif gm == 3: # 상시 기원
        return [
                True, # 상시 기원 여부
                [anytime.l_5star_char, anytime.l_5star_item], # 5성 캐릭터 항목, 5성 무기 항목
                [anytime.l_4star_char, anytime.l_4star_item], # 4성 캐릭터 항목, 4성 무기 항목
                anytime.l_3star_std, # 3성 일반 항목
                [anytime.huddle_5star_char, anytime.huddle_5star_item], # 5성 캐릭터 확률, 5성 무기 확률
                [anytime.huddle_4star_char, anytime.huddle_4star_item], # 4성 캐릭터 확률, 4성 무기 확률
                # 상시 기원의 확률 보정 관련 정보는 알려진 것이 없음
                # 일단은 캐릭터 기원과 동일한 수치를 사용하도록 해놓음
                [anytime.huddle_stack_5star, anytime.huddle_stack_5star_up], # 5성 확률 보정이 시작되는 스택 수, 보정되는 5성 확률
                [anytime.huddle_stack_4star, anytime.huddle_stack_4star_up], # 4성 확률 보정이 시작되는 스택 수, 보정되는 4성 확률
                [anytime.ceiling_5star, anytime.ceiling_4star] # 5성 천장, 4성 천장
               ]
    else:
        # db structure는 메시지 처리 초반부에 생성되므로
        # 여기서 가챠 모드를 가져오지 못한다면 에러가 맞음
        raise ValueError

def get_star(db, message, data, stack_huddle, stack_nothope): # 데이터, 데이터 A 반환 확률, 반천장 여부
    t = generate_random()
    random.seed(t)
    tn = random.randint(0, 4294967295) / 4294967295
    if tn >= 1 - stack_huddle or stack_nothope == 1:
        # 확정 천장을 뚫었거나 그렇지 않더라도 데이터 A 항목 반환 확률에 당첨된 경우
        return [random.choice(data[0]), 0]
    else:
        # 데이터 B 항목 반환, 반천장을 마킹해놓음
        return [random.choice(data[1]), 1]
        if res[0][0] == 5:
            db.set(str(message.author.id), "total_nothope_" + db.get(str(message.author.id), "gacha_mode"), str(int(db.get(str(message.author.id), "total_nothope_" + db.get(str(message.author.id), "gacha_mode"))) + 1)) # 통계 픽뚫 횟수 증가

def pull_calc(db, message, gacha_data, stack_5star_pull, stack_4star_pull, stack_5star_nothope, stack_4star_nothope):
    if stack_5star_pull == gacha_data[8][0]: # 5성 천장
        if gacha_data[0]: # 상시 기원(반천장 없음)인 경우
            return get_star(db, message, gacha_data[1], gacha_data[4][0], False)
        else: # 반천장이 있는 기원인 경우
            return get_star(db, message, gacha_data[1], gacha_data[4][0], stack_5star_nothope)
    elif stack_4star_pull == gacha_data[8][1]: # 4성 천장
        if gacha_data[0]: # 상시 기원(반천장 없음)인 경우
            return get_star(db, message, gacha_data[2], gacha_data[5][0], False)
        else: # 반천장이 있는 기원인 경우
            return get_star(db, message, gacha_data[2], gacha_data[5][0], stack_4star_nothope)
    else:
        # 5성 확률 처리
        if stack_5star_pull >= gacha_data[6][0]: # 5성 확률 보정 발동 시
            huddle_5star = 1 - gacha_data[6][1]
        else:
            huddle_5star = 1 - gacha_data[4][1]
        # 4성 확률 처리
        if stack_4star_pull >= gacha_data[7][0]: # 4성 확률 보정 발동 시
            huddle_4star = huddle_5star - gacha_data[7][1]
        else:
            huddle_4star = huddle_5star - gacha_data[5][1]
        # 랜덤 처리 시작
        t = generate_random()
        if t >= huddle_5star: # 5성 당첨 시
            if gacha_data[0]: # 상시 기원(반천장 없음)인 경우
                return get_star(db, message, gacha_data[1], gacha_data[4][0], False)
            else: # 반천장이 있는 기원인 경우
                return get_star(db, message, gacha_data[1], gacha_data[4][0], stack_5star_nothope)
        elif t >= huddle_4star: # 4성 당첨 시
            if gacha_data[0]: # 상시 기원(반천장 없음)인 경우
                return get_star(db, message, gacha_data[2], gacha_data[5][0], False)
            else: # 반천장이 잇는 기원인 경우
                return get_star(db, message, gacha_data[2], gacha_data[5][0], stack_4star_nothope)
        else: # 3성 당첨 시
            return [random.choice(gacha_data[3]), 0]

def pull(db, message):
    # 가챠 데이터를 가져옴
    gacha_data = get_gacha_mode(db, message)
    # 천장 관련 변수
    stack_5star_pull = int(db.get(str(message.author.id), "stack_5star_pull_" + db.get(str(message.author.id), "gacha_mode"))) # 5성 천장
    stack_4star_pull = int(db.get(str(message.author.id), "stack_4star_pull_" + db.get(str(message.author.id), "gacha_mode"))) # 4성 천장
    stack_5star_nothope = int(db.get(str(message.author.id), "stack_5star_nothope_" + db.get(str(message.author.id), "gacha_mode"))) # 5성 반천장 여부
    stack_4star_nothope = int(db.get(str(message.author.id), "stack_4star_nothope_" + db.get(str(message.author.id), "gacha_mode"))) # 4성 반천장 여부
    # 유저 통계 관련 변수
    total_pull = int(db.get(str(message.author.id), "total_pull_" + db.get(str(message.author.id), "gacha_mode"))) # 회차
    total_5star = int(db.get(str(message.author.id), "total_5star_" + db.get(str(message.author.id), "gacha_mode"))) # 5성 획득 횟수
    total_4star = int(db.get(str(message.author.id), "total_4star_" + db.get(str(message.author.id), "gacha_mode"))) # 4성 획득 횟수
    total_3star = int(db.get(str(message.author.id), "total_3star_" + db.get(str(message.author.id), "gacha_mode"))) # 3성 획득 횟수
    total_character = int(db.get(str(message.author.id), "total_character_" + db.get(str(message.author.id), "gacha_mode"))) # 캐릭터 획득 횟수
    total_item = int(db.get(str(message.author.id), "total_item_" + db.get(str(message.author.id), "gacha_mode"))) # 무기 획득 횟수
    # 가챠 처리 시작
    res = pull_calc(db, message, gacha_data, stack_5star_pull, stack_4star_pull, stack_5star_nothope, stack_4star_nothope)
    # 반천장 여부 작성
    if res[0][0] == 5:
        db.set(str(message.author.id), "stack_5star_nothope_" + db.get(str(message.author.id), "gacha_mode"), str(res[1]))
    elif res[0][0] == 4:
        db.set(str(message.author.id), "stack_4star_nothope_" + db.get(str(message.author.id), "gacha_mode"), str(res[1]))
    # 천장 스택, 통계 작성
    if res[0][0] == 5: # 5성을 획득한 경우
        db.set(str(message.author.id), "stack_5star_pull_" + db.get(str(message.author.id), "gacha_mode"), "0") # 5성 천장 스택 초기화
        db.set(str(message.author.id), "total_5star_" + db.get(str(message.author.id), "gacha_mode"), str(int(db.get(str(message.author.id), "total_5star_" + db.get(str(message.author.id), "gacha_mode"))) + 1)) # 5성 획득 횟수 추가
        if res[0][1] == 'character':
            db.set(str(message.author.id), "total_character_" + db.get(str(message.author.id), "gacha_mode"), str(int(db.get(str(message.author.id), "total_character_" + db.get(str(message.author.id), "gacha_mode"))) + 1)) # 캐릭터 획득 횟수 추가
        else:
            db.set(str(message.author.id), "total_item_" + db.get(str(message.author.id), "gacha_mode"), str(int(db.get(str(message.author.id), "total_item_" + db.get(str(message.author.id), "gacha_mode"))) + 1)) # 무기 획득 횟수 추가
    else:
        # 5성을 얻지 못한 경우 5성 천장 스택 추가
        db.set(str(message.author.id), "stack_5star_pull_" + db.get(str(message.author.id), "gacha_mode"), str(int(db.get(str(message.author.id), "stack_5star_pull_" + db.get(str(message.author.id), "gacha_mode"))) + 1))
    if res[0][0] == 4: # 4성을 획득한 경우
        db.set(str(message.author.id), "stack_4star_pull_" + db.get(str(message.author.id), "gacha_mode"), "0")
        db.set(str(message.author.id), "total_4star_" + db.get(str(message.author.id), "gacha_mode"), str(int(db.get(str(message.author.id), "total_4star_" + db.get(str(message.author.id), "gacha_mode"))) + 1))
        if res[0][1] == 'character':
            db.set(str(message.author.id), "total_character_" + db.get(str(message.author.id), "gacha_mode"), str(int(db.get(str(message.author.id), "total_character_" + db.get(str(message.author.id), "gacha_mode"))) + 1)) # 캐릭터 획득 횟수 추가
        else:
            db.set(str(message.author.id), "total_item_" + db.get(str(message.author.id), "gacha_mode"), str(int(db.get(str(message.author.id), "total_item_" + db.get(str(message.author.id), "gacha_mode"))) + 1)) # 무기 획득 횟수 추가
    else:
        # 4성을 얻지 못한 경우 4성 천장 스택 추가
        db.set(str(message.author.id), "stack_4star_pull_" + db.get(str(message.author.id), "gacha_mode"), str(int(db.get(str(message.author.id), "stack_4star_pull_" + db.get(str(message.author.id), "gacha_mode"))) + 1))
    if res[0][0] == 3: # 3성을 획득한 경우
        if res[0][1] == 'character':
            db.set(str(message.author.id), "total_character_" + db.get(str(message.author.id), "gacha_mode"), str(int(db.get(str(message.author.id), "total_character_" + db.get(str(message.author.id), "gacha_mode"))) + 1)) # 캐릭터 획득 횟수 추가
        else:
            db.set(str(message.author.id), "total_item_" + db.get(str(message.author.id), "gacha_mode"), str(int(db.get(str(message.author.id), "total_item_" + db.get(str(message.author.id), "gacha_mode"))) + 1)) # 무기 획득 횟수 추가
        db.set(str(message.author.id), "total_3star_" + db.get(str(message.author.id), "gacha_mode"), str(int(db.get(str(message.author.id), "total_3star_" + db.get(str(message.author.id), "gacha_mode"))) + 1)) # 무기 획득 횟수 추가
    # 회차 추가
    db.set(str(message.author.id), "total_pull_" + db.get(str(message.author.id), "gacha_mode"), str(int(db.get(str(message.author.id), "total_pull_" + db.get(str(message.author.id), "gacha_mode"))) + 1))
    return res[0]

def descript_pull(res):
    stars = ""
    typ = ""
    if res[0] == 5:
        stars = "★★★★★"
    elif res[0] == 4:
        stars = "★★★★☆"
    elif res[0] == 3:
        stars = "★★★☆☆"
    if res[1] == 'character':
        typ = "캐릭터"
    else:
        typ = "무기"
    if res[0] == 5:
        return "**" + stars + " " + typ + " : " + res[2] + "**"
    else:
        return stars + " " + typ + " : " + res[2]

def get_stat(db, message):
    if db.get(str(message.author.id), "gacha_mode") != "3":
        ret = [
            int(db.get(str(message.author.id), "total_pull_" + db.get(str(message.author.id), "gacha_mode"))),
            int(db.get(str(message.author.id), "total_5star_" + db.get(str(message.author.id), "gacha_mode"))),
            int(db.get(str(message.author.id), "total_4star_" + db.get(str(message.author.id), "gacha_mode"))),
            int(db.get(str(message.author.id), "total_3star_" + db.get(str(message.author.id), "gacha_mode"))),
            int(db.get(str(message.author.id), "total_character_" + db.get(str(message.author.id), "gacha_mode"))),
            int(db.get(str(message.author.id), "total_item_" + db.get(str(message.author.id), "gacha_mode"))),
            int(db.get(str(message.author.id), "total_nothope_" + db.get(str(message.author.id), "gacha_mode")))
        ]
    else:
        ret = [
            int(db.get(str(message.author.id), "total_pull_" + db.get(str(message.author.id), "gacha_mode"))),
            int(db.get(str(message.author.id), "total_5star_" + db.get(str(message.author.id), "gacha_mode"))),
            int(db.get(str(message.author.id), "total_4star_" + db.get(str(message.author.id), "gacha_mode"))),
            int(db.get(str(message.author.id), "total_3star_" + db.get(str(message.author.id), "gacha_mode"))),
            int(db.get(str(message.author.id), "total_character_" + db.get(str(message.author.id), "gacha_mode"))),
            int(db.get(str(message.author.id), "total_item_" + db.get(str(message.author.id), "gacha_mode"))),
            None
        ]
    return ret
