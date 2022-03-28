import sys

if __name__=="__main__":
    print("FATAL   : Run this bot from right way.")
    sys.exit(1)

data_name = "신의 주조 (2.6 전반부)"
data_ver = "2022032801"
run_date = "2022-03-30 ~ 2022-04-19"
stack_group = None

wishlists = [
                [ # 5성
                    [ # 픽업
                        [5, 'item', '하란 월백의 후츠'],
                        [5, 'item', '종말 탄식의 노래'],
                    ],
                    [ # 픽뚫
                        [5, 'item', '아모스의 활'],
                        [5, 'item', '천공의 날개'],
                        [5, 'item', '사풍 원서'],
                        [5, 'item', '천공의 두루마리'],
                        [5, 'item', '화박연'],
                        [5, 'item', '천공의 긍지'],
                        [5, 'item', '늑대의 말로'],
                        [5, 'item', '매의 검']
                    ]
                ],
                [ # 4성
                    [ # 픽업
                        [4, 'item', '피리검'],
                        [4, 'item', '제례 대검'],
                        [4, 'item', '용학살창'],
                        [4, 'item', '음유시인의 악장'],
                        [4, 'item', '녹슨 활']
                    ],
                    [ # 픽뚫
                        [4, 'character', '쿠죠 사라'],
                        [4, 'character', '연비'],
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
                        [4, 'character', '레이저'],
                        [4, 'character', '바바라'],
                        [4, 'item', '용의 포효'],
                        [4, 'item', '페보니우스 장창'],
                        [4, 'item', '제례의 악장'],
                        [4, 'item', '페보니우스 검'],
                        [4, 'item', '제례검'],
                        [4, 'item', '빗물 베기'],
                        [4, 'item', '소심'],
                        [4, 'item', '절현'],
                        [4, 'item', '페보니우스 비전'],
                        [4, 'item', '제례활'],
                        [4, 'item', '유야의 왈츠'],
                        [4, 'item', '시간의 검'],
                        [4, 'item', '페보니우스 대검'],
                        [4, 'item', '페보니우스 활']
                    ]
                ]
            ]

meta_prob = [
                0.75, # 5성 출현 시 픽업일 확률
                0.75, # 4성 출현 시 픽업일 확률
                0.007, # 천장 안찍고 5성 나올 확률
                0.06, # 천장 안찍고 4성 나올 확률
                62, # 5성 확률 보정 시작 시점
                0.32384, # 5성 확률 보정량
                8, # 4성 확률 보정 시작 시점
                0.5, # 4성 확률 보정량
                76, # 5성 천장
                9 # 4성 천장
            ]
