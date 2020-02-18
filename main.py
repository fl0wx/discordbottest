import os
from discord.ext import commands
from cogs.Greetings import Greetings

prefix = "?"
bot = commands.Bot(command_prefix=prefix)

BOT_TOKEN = os.environ['DISCORD_TOKEN']


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

bot.add_cog(Greetings(bot))
bot.run(BOT_TOKEN)
