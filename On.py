import discord


# 개발자 페이지에서 봇에 대한 토큰 텍스트를 가져온 뒤, TOKEN에 대입하자
TOKEN = "OTMyODk0NTgwNTY1NzQ1NjY1.YeZnyA.4jaDQwfIegG0pFyq2kJlGzV0hKw"

client = discord.Client()


# 봇이 접속하면 아래의 함수를 실행하게 된다
@client.event
async def on_ready():
    print(f'{client.user} online!')


# 봇을 실행하자
client.run('OTMyODk0NTgwNTY1NzQ1NjY1.YeZnyA.4jaDQwfIegG0pFyq2kJlGzV0hKw')