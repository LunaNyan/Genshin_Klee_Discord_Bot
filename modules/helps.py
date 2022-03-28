import discord

copyright_text = "ⓒ 2021, 2022 NEON MONSTERS, Genshin Impact ⓒ COGNOSPHERE PTE LTD. All Rights Reserved."
cver = "2.6" # 데이터베이스 버전
gver = "2.6" # 현재 게임 버전

def help(head, message, bot_ver, ifadmin, head2=None):
    if head2 == None:
        head2 = head
    m = message.content.replace(head + "도움 ", "")
    if m == "일반":
        embed = discord.Embed(title="일반 명령어 도움말")
        embed.add_field(name=head2 + "도움", value="이 도움말을 표시합니다.", inline=False)
        embed.add_field(name=head2 + "이용약관", value="이용약관을 표시합니다.", inline=False)
        embed.add_field(name=head2 + "제작자", value="제작자 정보를 표시합니다.", inline=False)
    elif m == "가챠":
        embed = discord.Embed(title="가챠 시뮬레이터 도움말")
        embed.add_field(name=head2 + "기원 (번호)", value="기원을 지정된 번호로 설정합니다.\n번호가 기입되지 않은 경우 목록을 표시합니다.", inline=False)
        embed.add_field(name=head2 + "목록 (페이지)", value="이전 기원을 목록으로 표시합니다.\n번호가 기입되지 않은 경우 1페이지의 목록을 표시합니다.", inline=False)
        embed.add_field(name=head2 + "단차 / " + head2 + "단챠", value="1회 뽑기를 진행합니다.", inline=False)
        embed.add_field(name=head2 + "연차 / " + head2 + "연챠", value="10회 뽑기를 진행합니다.", inline=False)
        embed.add_field(name=head2 + "5성 / " + head2 + "반천장", value="5성 항목이 나올 때까지 뽑기를 진행합니다.", inline=False)
        embed.add_field(name=head2 + "천장", value="5성 확률 UP 항목이 나올 때까지 뽑기를 진행합니다.\n확률 UP 항목이 없는 상시 기원에서는 사용할 수 없습니다.", inline=False)
        embed.add_field(name=head2 + "스택 (개수)[#]", value="스택 수를 설정합니다. 입력값 뒤에 '#'을 붙인 경우 반천장 픽뚫 상태를 마킹합니다.", inline=False)
        embed.add_field(name=head2 + "저격 (이름) / !명함 (이름)", value="입력된 항목이 나올 때까지 뽑기를 진행합니다.", inline=False)
        embed.add_field(name=head2 + "풀돌 (이름)", value="입력된 캐릭터를 풀돌(7번 당첨)할때까지 뽑기를 진행합니다.", inline=False)
        embed.add_field(name=head2 + "통계", value="저장된 통계를 표시합니다.", inline=False)
        embed.add_field(name=head2 + "정보", value="현재 선택된 기원의 정보를 표시합니다.", inline=False)
        embed.add_field(name=head2 + "견적 / " + head2 + "견적 (보유중인 원석 개수)", value="저장된 통계를 이용해 과금 견적서를 작성합니다.", inline=False)
        embed.add_field(name=head2 + "리셋", value="선택된 기원의 통계를 초기화합니다.", inline=False)
    elif m == "용어":
        embed = discord.Embed(title="용어집 도움말")
        embed.add_field(name=head2 + "용어", value="용어집에 수록된 용어 목록을 확인합니다.", inline=False)
        embed.add_field(name=head2 + "용어 (용어)", value="해당 용어에 대한 도움말을 표시합니다.", inline=False)
    elif m == "도구":
        embed = discord.Embed(title="편의 도구 도움말")
        embed.add_field(name=head2 + "재료", value="금일 파밍 가능한 육성 재료를 표시합니다.", inline=False)
        embed.add_field(name=head2 + "캐릭터 (캐릭터명)", value="캐릭터의 기본 정보를 확인합니다.", inline=False)
        embed.add_field(name=head2 + "레진 (레진 잔량)", value="레진 풀 충전까지 걸리는 시간을 계산합니다.", inline=False)
    elif m == "설정":
        embed = discord.Embed(title="설정 도움말")
        embed.add_field(name=head2 + "자동리셋", value="천장, 반천장 명령어 사용 시 처리 전에 통계를 초기화합니다.\n토글로 켜고 끌 수 있습니다.", inline=False)
        embed.add_field(name=head2 + "3성", value="천장/반천장/풀돌/저격 사용 시 출력되는 파일에 3성 아이템 출현 정보를 포함/제외합니다.\n토글로 켜고 끌 수 있습니다.", inline=False)
        embed.add_field(name=head2 + "시간제", value="시간 표시 방식을 12시간제 또는 24시간제로 토글합니다.\n기본값은 24시간제입니다.", inline=False)
    elif ifadmin and m == "관리자":
        embed = discord.Embed(title="관리자 도움말")
        embed.add_field(name=head2 + "공지채널", value="봇에 대한 공지사항을 게시할 채널을 지정합니다.", inline=False)
        embed.add_field(name=head2 + "접두어 (접두어)", value="명령어의 접두어를 지정합니다.", inline=False)
        embed.add_field(name="!접두어초기화", value="접두어를 초기화합니다.", inline=False)
    else:
        if head != "!" or head2 != None:
            ht = "현재 서버 접두어는 " + head2 + " 입니다.\n"
        else:
            ht = ""
        embed = discord.Embed(title="페보니우스 기사단의 「불꽃 기사」, 클레 등장!", description=ht + "[서포트 서버](https://discordapp.com/invite/6pgYMbC), [봇 초대하기](https://discord.com/oauth2/authorize?client_id=597782781673865216&scope=bot&permissions=0), [공식 트위터](https://twitter.com/neonmonsterskr), [문의 및 버그 리포트](https://docs.google.com/forms/d/e/1FAIpQLSfpgUc9Fl3dj2ESeb2w8ucaF-VlpQsiSozjfc8Y5UP9nyE92w/viewform?usp=sf_link)\n'!도움 (항목 이름)을 입력하면 명령어 목록을 볼 수 있어! (예시 : !도움 일반)")
        embed.add_field(name="일반", value="일반 명령어 모음", inline=False)
        embed.add_field(name="가챠", value="기원(가챠) 시뮬레이터 기능", inline=False)
        embed.add_field(name="도구", value="원신과 관련된 편의 기능", inline=False)
        embed.add_field(name="설정", value="명령어 개인 설정", inline=False)
        embed.add_field(name="용어", value="기원(가챠) 관련 용어에 대한 도움말", inline=False)
        if ifadmin:
            embed.add_field(name="관리자", value="서버 관리자 전용 기능", inline=False)
    embed.set_footer(text=copyright_text + ' | ver ' + bot_ver + "\n클레봇은 원신 공식 디스코드 봇이 아니며, COGNOSPHERE 및 HOYOVERSE와 연관이 없습니다.\n현재 원신 클라이언트 버전 : " + gver + ", 데이터베이스 버전 : " + cver)
    return embed

def helpg(head, message):
    m = message.content.replace(head + "용어 ", "")
    if m == "천장":
        text = "천장 시스템이란, 가챠 횟수에 상한선을 지정해 지정된 횟수(스택) 안에 무조건 레어 아이템을 얻도록 확률을 보정하는 시스템입니다."
        embed=discord.Embed(title="천장 시스템에 대한 도움말", description=text)
        text = "무기 픽업에서는 최대 **80연차 내에**, 이외에는 모두 최대 **90연차 내에** 무조건 5성 아이템이 출현합니다.\n"
        text += "또한, 10연차 내에 무조건 4성 아이템이 출현합니다."
        embed.add_field(name="가챠 횟수의 상한선(천장)", value=text, inline=False)
        text = "스택이 천장에 가까워질 수록 천장에 해당하는 등급의 아이템 출현 **확률이 대폭 증가**합니다.\n"
        text += "예를 들어, 캐릭터 픽업 기원에서는 74번째부터 5성 아이템 출현 확률이 0.6%에서 32.384%로 증가합니다."
        embed.add_field(name="숨겨진 확률 보정 시스템", value=text, inline=False)
    elif m == "돌파":
        text = "기원 과정에서 이미 있는 캐릭터를 중복 획득한 경우, 별자리 돌파를 하여 캐릭터의 특수 능력을 해금할 수 있습니다."
        embed=discord.Embed(title="별자리 돌파에 대한 도움말", description=text)
        text = "별자리 돌파는 최대 6개까지 가능하며, 모든 별자리를 돌파한 상태를 **풀돌**이라 부릅니다.\n"
        text += "별자리 돌파를 전혀 하지 않은 상태를 **명함**이라 부르며, 캐릭터를 획득만 하고 별자리 돌파를 하지 않은 상태로 기원을 중지하는 경우를 **명함만 뽑기**라고 합니다."
        embed.add_field(name="풀돌과 명함", value=text, inline=False)
    elif m == "스택":
        text = "스택이란, 가챠 시도 횟수를 기록하는 시스템입니다."
        embed=discord.Embed(title="스택에 대한 도움말", description=text)
        text = "가챠 횟수(스택)은 4성과 5성 스택이 있으며, 가챠를 진행할 때 동시에 증가합니다.\n"
        text += "스택은 해당 등급의 **아이템이 출현하는 시점에서 0으로 초기화**됩니다.\n"
        text += "또한, 모든 기원이 같은 스택을 공유하지 않고, **기원마다 따로 존재**합니다."
        text += "스택은 해당 기원이 업데이트 되더라도 **항상 유지**됩니다."
        embed.add_field(name="스택 관리", value=text, inline=False)
        text = "버전 2.3부터는 이벤트 일정에 따라 여러 개의 캐릭터 픽업 기원이 등장할 수 있습니다.\n"
        text += "이 경우 캐릭터 픽업 기원들은 **서로 스택을 공유합니다.**\n"
        text += "예를 들어, 하나의 캐릭터 픽업 기원에서 5성 캐릭터를 획득한 경우 다른 캐릭터 픽업 기원의 스택도 초기화됩니다.\n"
        text += "단, 모든 캐릭터 픽업 기원은 무기 픽업 기원, 상시 기원과는 스택을 공유하지 않습니다."
        embed.add_field(name="여러 개의 캐릭터 이벤트 기원", value=text, inline=False)
        text = "스택은 **기원 화면 하단의 뽑기 기록을 통해 확인**할 수 있으며, 페이지를 넘기며 획득한 아이템의 수를 세는 방식입니다.\n"
        embed.add_field(name="스택 확인 방법", value=text, inline=False)
    elif m == "픽업":
        text = "픽업 기원에는 확률 대폭 UP 아이템(픽업)이 지정된 확률을 선점하며, 나머지는 픽업이 아닌 아이템이 나눠 가집니다."
        embed=discord.Embed(title="반천장과 확정천장에 대한 도움말", description=text)
        text = "천장을 달성해 해당하는 아이템이 출현하는 과정에서 픽업이 아닌 아이템이 출현한 경우 이를 **픽뚫**이라 부르며, 동시에 **확정천장** 상태가 됩니다.\n"
        text += "이 확정천장 상태에서 다시 천장을 달성한 경우, 출현되는 아이템은 **무조건 픽업 아이템**입니다.\n"
        text += "또한, __픽업이 존재하지 않는 **상시 기원**에서는 확정 천장이 존재하지 않으며, 반천장만 사용됩니다.__"
        embed.add_field(name="픽업과 픽뚫", value=text, inline=False)
        text = "버전 2.0부터는 무기 픽업 기원에는 '신이 정한 궤도'라는 특수 시스템이 적용됩니다.\n"
        text+= "획득을 원하는 5성 무기를 선택한 후 무기 기원을 진행했을 때 **원하는 무기가 출현하지 않은 경우 '운명 경험치'를 하나 획득**합니다.\n"
        text+= "이 '운명 경험치'를 **2번 누적한 경우, 다음에 출현하는 무기는 __무조건 선택한 무기__**입니다.\n"
        text+= "추가로, 원하는 무기를 얻은 경우, 운명 경험치는 누적 개수와 상관없이 초기화됩니다."
        embed.add_field(name="신이 정한 궤도", value=text, inline=False)
        text = "픽업은 항상 **기간 한정**으로만 진행되며, 해당 기간이 아닌 경우 뽑으실 수 없습니다.\n"
        text += "따라서 원하는 5성 캐릭터나 무기가 현재 기원 이벤트로 진행중인 경우 **기간 안에 뽑으시는 것이 좋습니다.**\n"
        text += "예외로, 신규 4성 캐릭터는 출시 이후 다음 업데이트의 모든 기원에 일반 확률 아이템으로서 포함됩니다."
        embed.add_field(name="주의사항", value=text, inline=False)
    elif m == "화폐":
        text = "기원을 할 때는 인연이라는 아이템이 사용됩니다."
        embed=discord.Embed(title="기원 화폐에 대한 도움말", description=text)
        text = "__픽업 기원에는 뒤얽힌 인연__이, __초보자 추천 기원과 상시 기원에는 만남의 인연__이 사용됩니다.\n"
        text += "만약 기원에 사용되는 화폐를 잘못 산 경우 **환불 처리가 어려우니** 화폐 구매 시 신중하게 결정해야 합니다."
        embed.add_field(name="뒤얽힌 인연과 만남의 인연", value=text, inline=False)
        text = "인연은 개당 **160개의 원석 or 창세의 결정** 또는 **5개의 스타라이트** 또는 **75개의 스타더스트**로 구매할 수 있습니다.\n"
        text += "스타더스트로 인연을 구매하는 경우, 인연 당 **월 5개로 구매가 제한**됩니다."
        embed.add_field(name="인연을 구매하는 방법", value=text, inline=False)
        text = "창세의 결정은 현금 등을 통한 결제로 구매할 수 있으며, 원석과 1:1 비율로 교환이 가능합니다.\n"
        text += "창세의 결정은 엔트리 당 초기 구매 시 원래 제공량의 2배를 제공합니다. 해당되는 엔트리의 창세의 결정을 아직 구매하지 않은 경우를 **초회**라고 부릅니다.\n"
        text += "가장 높은 가격의 창세의 결정은 6480 + 1600개(119,000원)로, 속칭 **트럭**이라고 부르며, 대량 과금 시 자주 사용됩니다."
        embed.add_field(name="창세의 결정과 트럭", value=text, inline=False)
    elif m == "이벤트":
        text = "창세의 결정 구매 이외에도 많은 방법으로 원석을 쉽게 모을 수 있습니다."
        embed=discord.Embed(title="이벤트에 대한 도움말", description=text)
        text = "모험가 길드에서 제공하는 일일 퀘스트를 완료하여 매일 60개의 원석을 무료로 수집할 수 있습니다.\n"
        text += "30일간 매일 꼼꼼히 일일 퀘스트를 완료하면 **총 1,800개의 원석을 수집**할 수 있습니다."
        embed.add_field(name="일일 퀘스트", value=text, inline=False)
        text = "공월 축복은 5,900원에 판매 중이며, 구매 시 __창세의 결정 300개__를 받을 수 있으며 __30일간 매일 원석 90개__를 제공합니다.\n"
        text += "30일 간 매일 게임에 접속하여 꼼꼼히 원석을 받은 경우, **총 3000개의 원석을 수집**할 수 있습니다."
        embed.add_field(name="공월 축복", value=text, inline=False)
        text = "기행은 매일/매주/기행 기간 안에 해야 하는 미션을 달성해 레벨을 채우며 육성 소재와 만남의 인연을 획득하는 시스템입니다.\n"
        text += "기행 보상은 무료로 지급받을 수 있으나, 12,000원을 결제해 진주 기행 해금을 하면 **뒤얽힌 인연을 비롯한** 더 많은 보상을 획득할 수 있습니다.\n"
        text += "여기에 더해 15,000원을 추가 결제하여 진주의 노래를 해금하면 기행 레벨이 즉시 10레벨 증가하고, 기간 한정 프로필 명함을 획득할 수 있습니다.\n"
        text += "**진주 기행과 진주의 노래를 포함한 묶음 패키지를 25,000원에 구매**할 수도 있습니다."
        embed.add_field(name="기행", value=text, inline=False)
        text = "원신 공식 유튜브 채널에서 새 버전을 소개하는 방송을 진행할 때마다 **총 300원석 분량의 리딤코드**를 지급합니다.\n"
        text += "또한, 신규 버전 패치 후 서버 점검 보상으로 **300원석 분량의 사료**가 추가로 지급됩니다."
        embed.add_field(name="신규 버전 방송과 서버 점검 보상", value=text, inline=False)
        text = "이외에도 이벤트 및 임무 진행을 통해 소량의 원석을 획득할 수 있습니다.\n"
        text += "수집할 수 있는 원석의 양은 이벤트에 따라 상이합니다."
        embed.add_field(name="이벤트 및 임무 진행", value=text, inline=False)
        text = "설정 → 계정 → 교환코드를 통해 리딤 코드를 사용할 수 있습니다.\n"
        text += "리딤 코드는 계정 당 1회만 사용이 가능하며, 일부 리딤 코드는 사용 기한이 존재합니다.\n"
        text += "- GENSHINGIFT : 원석 * 50, 영웅의 경험 * 3"
        embed.add_field(name="기타", value=text, inline=False)
    else:
        embed = discord.Embed(title="용어집")
        embed.add_field(name="천장", value="가챠 천장과 확률 보정 시스템에 대한 이해", inline=False)
        embed.add_field(name="돌파", value="별자리 돌파와 명함", inline=False)
        embed.add_field(name="스택", value="가챠 시도 횟수를 기록해주는 시스템", inline=False)
        embed.add_field(name="픽업", value="픽업과 픽뚫, 반천장과 확정천장에 대한 설명", inline=False)
        embed.add_field(name="화폐", value="기원 시 사용되는 화폐 아이템에 대한 설명", inline=False)
        embed.add_field(name="이벤트", value="과금 비용을 줄이며 화폐를 수집하는 방법", inline=False)
    return embed

def tos():
    embed=discord.Embed(title="클레봇 이용 약관")
    text = "클레봇은 서비스 제공을 위해 아래 정보를 수집합니다.\n"
    text+= "- 작성자의 고유번호\n"
    text+= "- 봇이 반응하는 대화에 포함된 데이터\n"
    text+= "- 채팅이 보내진 시간\n"
    text+= "- 작성된 서버의 고유번호\n"
    text+= "- 작성된 서버내의 채널의 고유번호"
    embed.add_field(name="수집하는 정보", value=text, inline=False)
    text = "클레봇은 수집되는 정보를 본 용도로만 사용하며, 아래 명시된 용도 외에는 보관 및 사용되지 않습니다.\n"
    text+= "- 서비스 이용자 식별\n"
    text+= "- 서비스 제공을 위한 데이터베이스(기원 통계 등) 구축\n"
    text+= "- 제품 품질 관리, 오류 보고서 등의 이슈 트래킹\n"
    embed.add_field(name="수집된 정보의 사용", value=text, inline=False)
    text = "- 클레봇으로 실행하는 가챠는 **모두 모의 시뮬레이션입니다.** 봇의 가챠 시뮬레이션과 실제 가챠 진행 과정은 다를 수 있습니다.\n"
    text+= "- 데이터베이스 내 데이터는 원신 공식 네이버 카페, HoYoLAB, 인게임 내 정보를 기반으로 합니다. 원신 공식 콘텐츠 제작자 규정에 따라 **유출/데이터 마이닝/NDA(기밀 유지 계약서)를 위반하는 내용을 포함하는 콘텐츠는 __어떠한 추가 문의를 받더라도 등록이 불가능__**합니다.\n"
    text+= "- 봇과 관련된 문의 또는 게시 중단 요청은 [NEON MONSTERS 공식 트위터](https://twitter.com/neonmonsterskr)에 DM을 남겨주세요."
    embed.add_field(name="면책 사항", value=text, inline=False)
    embed.add_field(name="이용약관의 동의", value="본 봇을 그룹에 초대하는 행위를 한다면 본 약관에 동의한 것으로 간주합니다.", inline=False)
    embed.set_footer(text="특별한 사유가 있다면 관리자에게 문의해주시기 바랍니다.")
    return embed

def credits(client, bot_ver):
    embed=discord.Embed(title="원신 가챠 시뮬레이터 : 클레봇", color=0xffffff)
    embed.add_field(name="유용한 링크", value="[민원창구](https://discordapp.com/invite/6pgYMbC), [봇 초대하기](https://discord.com/oauth2/authorize?client_id=597782781673865216&scope=bot&permissions=0), [공식 트위터](https://twitter.com/neonmonsterskr), [문의 및 버그 리포트](https://docs.google.com/forms/d/e/1FAIpQLSfpgUc9Fl3dj2ESeb2w8ucaF-VlpQsiSozjfc8Y5UP9nyE92w/viewform?usp=sf_link)", inline=False)
    embed.add_field(name="제작자", value="프로젝트 주 책임자 : libertin\n프로그래머 : libertin, bad_guy, ComputerLove\n운영 및 인프라 관리 : back-step\n품질 관리 및 이슈 트래킹 : KidNextDoor", inline=False)
    embed.add_field(name="특별 감사", value="케어\n빛깔눈꽃\nFOX-B", inline=False)
    embed.add_field(name="봇 시스템 버전", value="SKY1-20211219-A2", inline=False)
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.set_footer(text=copyright_text + ' | ver ' + bot_ver + "\n클레봇은 원신 공식 디스코드 봇이 아니며, COGNOSPHERE 및 HOYOVERSE와 연관이 없습니다.\n현재 원신 클라이언트 버전 : " + gver + ", 데이터베이스 버전 : " + cver)
    return embed

def welcome_message(client, bot_ver):
    text = "클레봇은 원신을 플레이하는 유저들을 위해 가챠 시뮬레이터 등 각종 편의 기능을 제공합니다.\n사용할 수 있는 기능은 '!도움'을 입력하여 확인할 수 있습니다."
    embed=discord.Embed(title="클레봇을 초대해주셔서 감사합니다!", description=text)
    text = "'!이용약관'을 입력하여 나오는 글을 숙지하여 주시기 바랍니다.\n봇과 관련된 공지사항은 최근에 명령어를 사용한 채널로 지정됩니다. 고정을 원하시는 경우 해당 채널에서 '!공지채널'을 입력해주세요."
    embed.add_field(name="사용하기 전에", value=text)
    embed.set_footer(text=copyright_text + ' | ver ' + bot_ver + "\n클레봇은 원신 공식 디스코드 봇이 아니며, COGNOSPHERE 및 HOYOVERSE와 연관이 없습니다.")
    embed.set_thumbnail(url=client.user.avatar_url)
    return embed
