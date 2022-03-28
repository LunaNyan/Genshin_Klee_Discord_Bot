import sys

if __name__=="__main__":
    print("FATAL   : Run this bot from right way.")
    sys.exit(1)

data_name = "잔에 담긴 시 (1.0)"
data_ver = "2021062801"
run_date = "2020-09-28 ~ 2020-10-18"
stack_group = None

wishlists = [
                [ # 5성
                    [ # 픽업
                        [5, 'character', '벤티']
                    ],
                    [ # 픽뚫
                        [5, 'character', '각청'],
                        [5, 'character', '모나'],
                        [5, 'character', '치치'],
                        [5, 'character', '다이루크'],
                        [5, 'character', '진']
                    ]
                ],
                [ # 4성
                    [ # 픽업
                        [4, 'character', '바바라'],
                        [4, 'character', '피슬'],
                        [4, 'character', '향릉']
                    ],
                    [ # 픽뚫
                        [4, 'character', '행추'],
                        [4, 'character', '노엘'],
                        [4, 'character', '설탕'],
                        [4, 'character', '북두'],
                        [4, 'character', '응광'],
                        [4, 'character', '베넷'],
                        [4, 'character', '중운'],
                        [4, 'character', '레이저'],
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
                ]
            ]

meta_prob = [
                0.5, # 5성 출현 시 픽업일 확률
                0.5, # 4성 출현 시 픽업일 확률
                0.006, # 천장 안찍고 5성 나올 확률
                0.051, # 천장 안찍고 4성 나올 확률
                73, # 5성 확률 보정 시작 시점
                0.32384, # 5성 확률 보정량
                8, # 4성 확률 보정 시작 시점
                0.5, # 4성 확률 보정량
                89, # 5성 천장
                9 # 4성 천장
            ]