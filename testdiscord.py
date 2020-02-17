from discord.ext import commands
prefix = "?"
bot = commands.Bot(command_prefix=prefix)


@bot.event
async def on_ready():
    print("Everything's all ready to go~")


@bot.command()
async def ping(ctx):
    '''
    This text will be shown in the help command
    '''

    # Get the latency of the bot
    latency = bot.latency  # Included in the Discord.py library
    # Send it to the user
    await ctx.send(latency)


@bot.command()
async def echo(ctx, *, content:str):
    await ctx.send(content)


bot.run('Njc4MzQ0NzMxMjI2NTM4MDA0.Xkhmhg.EX5sBvoRYWXQFFxahKT21npsPNk')
