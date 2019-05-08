from discord.ext import commands
from discord.utils import get
from discord import FFmpegPCMAudio

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
    def unlock():
        nonlocal lock
        lock = False

    lock = True
    channel = ctx.message.mentions[0].voice.channel
    voice = get(bot.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()

    voice.play(FFmpegPCMAudio('crusade.mp3'), after=unlock())
    await ctx.send("We'll take the Jerusalem")

    print(lock)
    while lock:
        print("fdvfsda")
        if channel != ctx.message.mentions[0].voice.channel:
            print("afdvbdfgfd")


bot.run('NTczNDYwMDkyNzY3MTc0NjU4.XMrLXA.wC9mxCltb0gtT2xLO0nSRObvGRQ')