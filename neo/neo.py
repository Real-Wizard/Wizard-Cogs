import discord
from discord.ext import commands
import random
from urllib.parse import quote_plus
from enum import Enum
from .utils.chat_formatting import *
from .utils.chat_formatting import escape_mass_mentions, italics, pagify
from random import randint
from random import choice
from random import choice as randchoice
import datetime
from __main__ import send_cmd_help
import re
import urllib
import time
import aiohttp
from .utils import checks
import asyncio
from cogs.utils.dataIO import dataIO
import io, os
from .utils.dataIO import fileIO
import logging

class emotes:
    def __init__(self, bot):
		self.bot = bot
		
		
	@commands.command(pass_context=True)
	async def el(self, ctx):
		"""EL"""
        emojis =  []
        while x < len([r for r in ctx.message.server.emojis]) -1:
            x = x + 1
            emojis.append("<:{}:{}>".format([r.name for r in ctx.message.server.emojis][x], [r.id for r inctx.message.server.emojis[x]))
        if server.emojis:
            emotes = discord.Embed(title="Emotes", description=" ".join(emojis), colour=discord.Colour(value=colour))
        else:
            emotes = discord.Embed(title="Emotes", description="NONE", colour=discord.Colour(value=colour))
		await self.bot.say(embed=emotes)
		
def setup(bot):
	bot.add_cog(emotes(bot))
    
