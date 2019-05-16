from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio
from discord.ext.commands.errors import CommandInvokeError

import asyncio

bot = commands.Bot(command_prefix="-")


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.command(description="Samba bro")
async def samba(ctx):
    print("dasfs")
    url = "https://dupa.com"
    author = ctx.message.author
    channel = author.voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice.play(FFmpegPCMAudio('szamba.mp3'), after=lambda: ctx.send("Szamba!!!"))


@bot.command(description="In the name of God", pass_context=True)
async def crusade(ctx):
    channel = ctx.message.mentions[0].voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice.play(FFmpegPCMAudio('crusade.mp3'))
    await ctx.send("We'll take Jerusalem")

    for i in range(1000):
        await asyncio.sleep(1)
        try:
            if channel != ctx.message.mentions[0].voice.channel:
                channel = ctx.message.mentions[0].voice.channel
                await voice.move_to(channel)
        except AttributeError as ex:
            print(type(ex))

bot.run('NTc1NzU1NTIzNzYxMTExMDg2.XNMkIg.WdMcJFQTK8wniCyyuFWcXUtfJNY')