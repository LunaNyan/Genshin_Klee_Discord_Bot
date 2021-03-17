# 캐릭터 픽업 기원 데이터
# 제작 : libertin (2021-03-15)
# 2021 STUDIO ONE

import sys

if __name__=="__main__":
    print("FATAL   : Run this bot from right way.")
    sys.exit(1)

data_name = "잔에 담긴 시"
data_ver = "2021031701"

# 5성 확률UP 항목
l_5star_up = [
                [5, 'character', '벤티', True]
             ]

# 5성 일반 확률 항목
l_5star_std = [
                [5, 'character', '각청', False],
                [5, 'character', '모나', False],
                [5, 'character', '치치', False],
                [5, 'character', '다이루크', False],
                [5, 'character', '진', False]
            ]

# 4성 확률 UP 항목
l_4star_up = [
                [4, 'character', '설탕', True],
                [4, 'character', '노엘', True],
                [4, 'character', '레이저', True],
           ]

# 4성 일반 확률 항목
l_4star_std = [
                [4, 'character', '신염', False],
                [4, 'character', '디오나', False],
                [4, 'character', '중운', False],
                [4, 'character', '베넷', False],
                [4, 'character', '피슬', False],
                [4, 'character', '응광', False],
                [4, 'character', '북두', False],
                [4, 'character', '행추', False],
                [4, 'character', '향릉', False],
                [4, 'item', '녹슨 활', False],
                [4, 'item', '제례활', False],
                [4, 'item', '절현', False],
                [4, 'item', '페보니우스 활', False],
                [4, 'item', '소심', False],
                [4, 'item', '제례의 악장', False],
                [4, 'item', '음유시인의 악장', False],
                [4, 'item', '페보니우스 비전', False],
                [4, 'item', '페보니우스 장창', False],
                [4, 'item', '용학살창', False],
                [4, 'item', '빗물 베기', False],
                [4, 'item', '제례 대검', False],
                [4, 'item', '시간의 검', False],
                [4, 'item', '페보니우스 대검', False],
                [4, 'item', '용의 포효', False],
                [4, 'item', '제례검', False],
                [4, 'item', '피리검', False],
                [4, 'item', '페보니우스 검', False]
            ]

# 3성 항목
l_3star_std = [
                [3, 'item', '탄궁', False],
                [3, 'item', '신궁의 서약', False],
                [3, 'item', '까마귀깃 활', False],
                [3, 'item', '비취 오브', False],
                [3, 'item', '드래곤 슬레이어 영웅담', False],
                [3, 'item', '마도 서론', False],
                [3, 'item', '흑술창', False],
                [3, 'item', '훌륭한 대화수단', False],
                [3, 'item', '드래곤 블러드 소드', False],
                [3, 'item', '강철의 그림자', False],
                [3, 'item', '비천어검', False],
                [3, 'item', '여명신검', False],
                [3, 'item', '차가운 칼날', False]
            ]

huddle_5star_up = 0.5
huddle_4star_up = 0.5
huddle_5star = 0.006
huddle_4star = 0.051
huddle_stack_5star = 73
huddle_stack_5star_up = 0.32384
huddle_stack_4star = 8
huddle_stack_4star_up = 0.5
ceiling_5star = 89
ceiling_4star = 9