import discord
import os
from SingleSymbolExecutor import execute
from discord.ext import commands
intents = discord.Intents().all()
client = commands.Bot(command_prefix='!', intents=intents)
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="the market"))

@client.event
async def on_message(message):
    try:
        if message.content.startswith("!"):
            symbol = message.content[1:]
            output_path = execute(symbol)
            with open(output_path, "rb") as f:
                await message.channel.send(file=discord.File(f))
            os.remove(output_path)
    except:
        await message.channel.send(f'Im sorry, there was a problem with that Symbol being processed. Please let Jae know if this is unexpected.')
client.run("MTA2NTMxNTIxNTgyNDEzODMzMQ.G5hyMr.Ul5J7Lc-hiZYvWZhKchvLzDTJ5uC_q9pfIH7XE")
