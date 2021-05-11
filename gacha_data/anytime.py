# 상시 기원 데이터
# 제작 : libertin (2021-03-15)
# 2021 STUDIO ONE

import sys

if __name__=="__main__":
    print("FATAL   : Run this bot from right way.")
    sys.exit(1)

data_name = "세상 여행"
data_ver = "2021042801"

# 5성 캐릭터 항목
l_5star_char = [
                [5, 'character', '각청'],
                [5, 'character', '모나'],
                [5, 'character', '치치'],
                [5, 'character', '다이루크'],
                [5, 'character', '진']
               ]

# 5성 무기 항목
l_5star_item = [
                [5, 'item', '아모스의 활'],
                [5, 'item', '천공의 날개'],
                [5, 'item', '사풍 원서'],
                [5, 'item', '천공의 두루마리'],
                [5, 'item', '화박연'],
                [5, 'item', '천공의 마루'],
                [5, 'item', '늑대의 말로'],
                [5, 'item', '천공의 긍지'],
                [5, 'item', '천공의 검'],
                [5, 'item', '매의 검']
               ]

# 4성 캐릭터 항목
l_4star_char = [
                [4, 'character', '로자리아'],
                [4, 'character', '신염'],
                [4, 'character', '설탕'],
                [4, 'character', '디오나'],
                [4, 'character', '중운'],
                [4, 'character', '노엘'],
                [4, 'character', '베넷'],
                [4, 'character', '피슬'],
                [4, 'character', '응광'],
                [4, 'character', '행추'],
                [4, 'character', '북두'],
                [4, 'character', '향릉'],
                [4, 'character', '엠버'],
                [4, 'character', '레이저'],
                [4, 'character', '케이아'],
                [4, 'character', '리사'],
                [4, 'character', '바바라']
               ]

# 4성 무기 항목
l_4star_item = [
                [4, 'item', '녹슨 활'],
                [4, 'item', '제례활'],
                [4, 'item', '절현'],
                [4, 'item', '페보니우스 활'],
                [4, 'item', '소심'],
                [4, 'item', '제례의 악장'],
                [4, 'item', '음유시인의 악장'],
                [4, 'item', '페보니우스 비전'],
                [4, 'item', '페보니우스 장창'],
                [4, 'item', '용학살창'],
                [4, 'item', '빗물 베기'],
                [4, 'item', '제례 대검'],
                [4, 'item', '시간의 검'],
                [4, 'item', '페보니우스 대검'],
                [4, 'item', '용의 포효'],
                [4, 'item', '제례검'],
                [4, 'item', '피리검'],
                [4, 'item', '페보니우스 검']
               ]

# 3성 항목
l_3star_std = [
                [3, 'item', '탄궁'],
                [3, 'item', '신궁의 서약'],
                [3, 'item', '까마귀깃 활'],
                [3, 'item', '비취 오브'],
                [3, 'item', '드래곤 슬레이어 영웅담'],
                [3, 'item', '마도 서론'],
                [3, 'item', '흑술창'],
                [3, 'item', '훌륭한 대화수단'],
                [3, 'item', '드래곤 블러드 소드'],
                [3, 'item', '강철의 그림자'],
                [3, 'item', '비천어검'],
                [3, 'item', '여명신검'],
                [3, 'item', '차가운 칼날']
            ]

huddle_5star_char = 0.003
huddle_5star_item = 0.003
huddle_4star_char = 0.0255
huddle_4star_item = 0.0255
huddle_stack_5star = 73
huddle_stack_5star_up = 0.32384
huddle_stack_4star = 8
huddle_stack_4star_up = 0.5
ceiling_5star = 89
ceiling_4star = 9