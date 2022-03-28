import sys

if __name__=="__main__":
    print("FATAL   : Run this bot from right way.")
    sys.exit(1)

data_name = "세상 여행"
data_ver = "2.1-2021092501"
run_date = "2020-09-28 ~ 영구 지속"
stack_group = None

wishlists = [
                [ # 5성
                    [ # 캐릭터
                        [5, 'character', '각청'],
                        [5, 'character', '모나'],
                        [5, 'character', '치치'],
                        [5, 'character', '다이루크'],
                        [5, 'character', '진']
                    ],
                    [ # 무기
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
                ],
                [ # 4성
                    [ # 캐릭터
                        [4, 'character', '운근'],
                        [4, 'character', '토마'],
                        [4, 'character', '쿠죠 사라'],
                        [4, 'character', '사유'],
                        [4, 'character', '로자리아'],
                        [4, 'character', '레이저'],
                        [4, 'character', '베넷'],
                        [4, 'character', '바바라'],
                        [4, 'character', '설탕'],
                        [4, 'character', '피슬'],
                        [4, 'character', '연비'],
                        [4, 'character', '신염'],
                        [4, 'character', '행추'],
                        [4, 'character', '북두'],
                        [4, 'character', '디오나'],
                        [4, 'character', '중운'],
                        [4, 'character', '노엘'],
                        [4, 'character', '응광'],
                        [4, 'character', '향릉'],
                        [4, 'character', '엠버'],
                        [4, 'character', '리사'],
                        [4, 'character', '케이아']
                    ],
                    [ # 무기
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
                0.5, # 5성 출현 시 캐릭터일 확률
                0.5, # 4성 출현 시 캐릭터일 확률
                0.006, # 천장 안찍고 5성 나올 확률
                0.051, # 천장 안찍고 4성 나올 확률
                73, # 5성 확률 보정 시작 시점
                0.32384, # 5성 확률 보정량
                8, # 4성 확률 보정 시작 시점
                0.5, # 4성 확률 보정량
                89, # 5성 천장
                9 # 4성 천장
            ]
