import sys

if __name__=="__main__":
    print("FATAL   : Run this bot from right way.")
    sys.exit(1)

import discord

copyright_text = "ⓒ 2021 STUDIO ONE"

def help(bot_ver):
    embed = discord.Embed(title="페보니우스 기사단의 「불꽃 기사」, 클레 등장!")
    embed.add_field(name="!도움", value="이 도움말을 표시합니다.", inline=False)
    embed.add_field(name="!기원 (번호)", value="기원을 지정된 번호로 설정합니다.\n번호가 기입되지 않은 경우 목록을 표시합니다.", inline=False)
    embed.add_field(name="!단차 / !단챠", value="1회 뽑기를 진행합니다.", inline=False)
    embed.add_field(name="!연차 / !연챠", value="10회 뽑기를 진행합니다.", inline=False)
    embed.add_field(name="!5성 / !반천장", value="5성 항목이 나올 때까지 뽑기를 진행합니다.", inline=False)
    embed.add_field(name="!천장", value="5성 확률 UP 항목이 나올 때까지 뽑기를 진행합니다.\n확률 UP 항목이 없는 상시 기원에서는 5성 캐릭터가 나올 때까지 뽑기를 진행합니다.", inline=False)
    embed.add_field(name="!통계", value="저장된 통계를 표시합니다.", inline=False)
    #embed.add_field(name="!견적", value="저장된 통계를 이용해 과금 견적서를 작성합니다.", inline=False)
    embed.add_field(name="!리셋", value="통계를 초기화합니다.", inline=False)
    embed.set_footer(text=copyright_text + ' | ver ' + bot_ver)
    return embed