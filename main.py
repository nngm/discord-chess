import discord
import chess

import __token__

board = chess.Board()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def fen(FEN: str):
    res = ''
    cnt = 0
    flag = True

    for c in FEN:
        if c.isdecimal():
            for _ in range(int(c)):
                res += '<e' + 'wb'[cnt % 2] + 's>'
                cnt += 1
        else:
            if c == '/':
                res += '\n'
                cnt += 1
                continue
            elif c not in 'KkQqRrBbNnPp':
                flag = False
                break

            if c.isupper():
                res += '<w'
                c = c.lower()
            else:
                res += '<b'
            res += c + 'wb'[cnt % 2] + '>'
            cnt += 1

    emoji = {
        '<ews>': '<:ews:1129054706463944844>',
        '<ebs>': '<:ebs:1129054662297931826>',
        '<wkw>': '<:wkw:1129054659206725683>',
        '<wkb>': '<:wkb:1129054655578656800>',
        '<bkw>': '<:bkw:1129054653779296256>',
        '<bkb>': '<:bkb:1129054650952335511>',
        '<wqw>': '<:wqw:1129054648729354331>',
        '<wqb>': '<:wqb:1129054645264855133>',
        '<bqw>': '<:bqw:1129054641640964136>',
        '<bqb>': '<:bqb:1129054639644491937>',
        '<wrw>': '<:wrw:1129054636658143302>',
        '<wrb>': '<:wrb:1129054632639991879>',
        '<brw>': '<:brw:1129054630769332305>',
        '<brb>': '<:brb:1129054627317424240>',
        '<wbw>': '<:wbw:1129054625727783012>',
        '<wbb>': '<:wbb:1129054622556889098>',
        '<bbw>': '<:bbw:1129054618131898450>',
        '<bbb>': '<:bbb:1129054615585951804>',
        '<wnw>': '<:wnw:1129054613434286100>',
        '<wnb>': '<:wnb:1129054610053664781>',
        '<bnw>': '<:bnw:1129054607956520983>',
        '<bnb>': '<:bnb:1129054603883843664>',
        '<wpw>': '<:wpw:1129054601975447592>',
        '<wpb>': '<:wpb:1129054598892626002>',
        '<bpw>': '<:bpw:1129054597323960492>',
        '<bpb>': '<:bpb:1129054593653952663>',
    }

    for key, value in emoji.items():
        res = res.replace(key, value)

    return res

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    global board
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
	
    if message.content == 'start':
        board = chess.Board()
        await message.channel.send(fen(board.fen()))

    if message.content.startswith('move'):
        board.push_san(message.content.split()[1])
        await message.channel.send(fen(board.fen()))
        if board.outcome():
            await message.channel.send(board.outcome().result())

    if message.content == 'undo':
        board.pop()
        await message.channel.send(fen(board.fen()))

client.run(__token__.token)

