
import discord
import asyncio
import random

from discord import message

client = discord.Client()

token = 'OTMyODk0NTgwNTY1NzQ1NjY1.YeZnyA.4jaDQwfIegG0pFyq2kJlGzV0hKw' #봇 토큰

@client.event
async def on_ready():

    print(client.user.name)
    print('성공적으로 봇이 시작되었습니다')
    game = discord.Game('~하는 중') #봇 ~하는중 입력
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "봇하": #내가 '봇하'이라고 말하면
        await message.channel.send (f"봇하!") #봇이 '봇하!'라고 대답

client.run('OTMyODk0NTgwNTY1NzQ1NjY1.YeZnyA.4jaDQwfIegG0pFyq2kJlGzV0hKw')