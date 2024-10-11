import discord
import guess
import auto
import rps
import warns
import url
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True #reading messages
bot = commands.Bot(command_prefix='!', intents=intents)


from guess import setup as guess_setup
guess_setup(bot)

from auto import setup as auto_setup
auto_setup(bot)

from rps import setup as rps_setup
rps_setup(bot)

from warns import setup as warn_setup
warn_setup(bot)

from url import setup as url_setup
url_setup(bot)

bot.run('TOKEN')