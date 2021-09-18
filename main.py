from datetime import date, datetime
from pathlib import Path

import aiocron
import discord
import logging
import os
import youtube_dl

from discord.ext import commands
from src.components.music import Music

# Silence useless bug reports messages
youtube_dl.utils.bug_reports_message = lambda: ''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix=['--'], description='ROCKU', intents=intents, help_command=None)


bot.add_cog(Music(bot))

@bot.event
async def on_ready():
  print(datetime.now().time())
  print(datetime.today().strftime('%m/%d'))
  print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(bot))

@bot.event
async def on_message_delete(message):
  chn = bot.get_channel(int(os.getenv("DISCORD_MSG_LOG")))
  embed = discord.Embed(title='DELETED MESSAGE', color=discord.Color.red())
  embed.set_author(name=str(message.author))
  embed.add_field(name="Message", value=message.content)
  embed.set_footer(text="Channel Origin - {}".format(str(message.channel)))
  await chn.send(embed=embed)

# @aiocron.crontab('0 14 * * *')
# async def birthday():
#   cd = datetime.today().strftime('%m/%d').split("/")
#   month = int(cd[0])
#   day = int(cd[1])
#   channel = bot.get_channel(int(os.getenv("DISCORD_GENERAL")))

#   for key, value in birthday_db.list_birthdays():
#     bd = value["birthday"].split("/")
#     if month == int(bd[0]) and day == int(bd[1]):
#       cb = value["celebrant_id"]
#       await channel.send("It's <@{}>'s birthday today! Happy birthday desu nyah~ uwu :birthday: :confetti_ball:".format(cb))
#       await channel.send(file=discord.File('./src/res/bd.jpg'))

# @aiocron.crontab('0 22 * * sun')
# async def crystal_chunks_and_parametric():
#   channel = bot.get_channel(int(os.getenv("DISCORD_GACHA_GAMES")))
#   ping = "<@&{}>".format(os.getenv("DISCORD_CRYSTAL_CHUNKS"))
 
#   await channel.send(ping, file=discord.File('./src/res/cc_2.png'))
#   await channel.send("<@&{}> Also, don't forget to use the parametric transformer for this week! uwu".format(os.getenv("DISCORD_GENSHIN_COOP")))

bot.run(os.getenv("TOKEN"))
