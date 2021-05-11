import sys

if __name__=="__main__":
    print("FATAL   : Run this bot from right way.")
    sys.exit(1)

import discord

copyright_text = "ⓒ 2021 STUDIO ONE, Genshin Impact & ⓒ 2020 miHoYo All Rights Reserved."

def help(bot_ver):
    embed = discord.Embed(title="페보니우스 기사단의 「불꽃 기사」, 클레 등장!", description="[서포트 서버](https://discordapp.com/invite/6pgYMbC)")
    embed.add_field(name="!도움", value="이 도움말을 표시합니다.", inline=False)
    embed.add_field(name="!버전", value="버전 정보를 표시합니다.", inline=False)
    embed.add_field(name="!이용약관", value="이용약관을 표시합니다.", inline=False)
    embed.add_field(name="!제작자", value="제작자 정보를 표시합니다.", inline=False)
    embed.add_field(name="!기원 (번호)", value="기원을 지정된 번호로 설정합니다.\n번호가 기입되지 않은 경우 목록을 표시합니다.", inline=False)
    embed.add_field(name="!단차 / !단챠", value="1회 뽑기를 진행합니다.", inline=False)
    embed.add_field(name="!연차 / !연챠", value="10회 뽑기를 진행합니다.", inline=False)
    embed.add_field(name="!5성 / !반천장", value="5성 항목이 나올 때까지 뽑기를 진행합니다.", inline=False)
    embed.add_field(name="!천장", value="5성 확률 UP 항목이 나올 때까지 뽑기를 진행합니다.\n확률 UP 항목이 없는 상시 기원에서는 사용할 수 없습니다.", inline=False)
    embed.add_field(name="!저격 (이름)", value="입력된 항목이 나올 때까지 뽑기를 진행합니다.", inline=False)
    embed.add_field(name="!풀돌 (이름)", value="입력된 캐릭터를 풀돌(7번 당첨)할때까지 뽑기를 진행합니다.", inline=False)
    embed.add_field(name="!통계", value="저장된 통계를 표시합니다.", inline=False)
    embed.add_field(name="!견적 / !견적 (보유중인 원석 개수)", value="저장된 통계를 이용해 과금 견적서를 작성합니다.", inline=False)
    embed.add_field(name="!리셋", value="선택된 기원의 통계를 초기화합니다.", inline=False)
    embed.add_field(name="!자동리셋", value="천장, 반천장 명령어 사용 시 처리 전에 통계를 초기화합니다.\n토글로 켜고 끌 수 있습니다.", inline=False)
    embed.set_footer(text=copyright_text + ' | ver ' + bot_ver)
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
    embed.add_field(name="이용약관의 동의", value="본 봇을 그룹에 초대하는 행위를 한다면 본 약관에 동의한 것으로 간주합니다.", inline=False)
    embed.set_footer(text="특별한 사유가 있다면 관리자에게 문의해주시기 바랍니다.")
    return embed

def credits(client, bot_ver):
    embed=discord.Embed(title="원신 가챠 시뮬레이터 : 클레봇", color=0xffffff)
    embed.add_field(name="유용한 링크", value="[민원창구](https://discordapp.com/invite/6pgYMbC), [봇 초대하기](https://discord.com/oauth2/authorize?client_id=597782781673865216&scope=bot&permissions=0)", inline=False)
    embed.add_field(name="프로그래머", value="libertin", inline=False)
    embed.add_field(name="인프라 및 시스템 관리자", value="back-step\n라이젠쇼군", inline=False)
    embed.set_thumbnail(url=client.user.avatar_url)
    embed.set_footer(text=copyright_text + " | ver " + bot_ver)
    return embed