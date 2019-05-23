import discord
import re

client = discord.Client()


@client.event
async def on_ready():
    print('ログインしました')


@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return
    if not message.clean_content.startswith('/multi'):
        return


def validateMessageAsMultiBattleRequest(message: str) -> bool:
    splitted = message.splitlines()
    print(splitted)
    if not splitted:
        return False
    if not splitted[0] == '/multi':
        return False
    if len(splitted) < 4:
        return False
    if splitted[2]:
        return validateDateTimeOrEmpty(splitted[2])
    return True


def validateDateTimeOrEmpty(text: str) -> bool:
    regexp = r'\d{1,2}/\d{1,2}\s([0-1][0-9]|2[0-3])\:[0-5][0-9]'
    spl = text.split(' ~ ')
    print(spl)
    res = True
    for _idx, item in enumerate(spl):
        print(item)
        if not item:
            break
        if not re.search(regexp, item):
            res = False

    return res


with open('./example.txt') as f:
    message = f.read()
    print(message)
    s = validateMessageAsMultiBattleRequest(message)
    print(s)
