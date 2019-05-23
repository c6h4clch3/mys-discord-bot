import discord
import re
import datetime
from parseMessage import parseMessage

client = discord.Client()

TOKEN = ''
with open('discord_token') as f:
    TOKEN = f.read()

print(TOKEN)


@client.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    await test(message)


async def test(message: discord.Message):
    if str(message.channel) != 'general':
        return
    if not message.clean_content.startswith('/test'):
        return
    await message.channel.send('テストだからってよ......止まるんじゃ、ねぇぞ.....')

async def registerMulti(message: discord.Message):
    if str(message.channel) != '共闘マルチ募集':
        return
    if not message.clean_content.startswith('/multi'):
        return

    parsed = parseMessage(message.clean_content)
    title = parsed[0]
    datetimes = parsed[1]
    description = parsed[2]

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


client.run(TOKEN)
