import discord
import time
from discord.ext import commands
from random import choice, randint
import cogs.utils
import asyncio
from cogs.utils import checks

__author__ = "MasterKnight"
class rainbow:
    """Rainbows the selected role"""

    def __init__(self, bot):
        self.bot = bot
    @checks.admin_or_permissions(administrator=True)
    @commands.command(pass_context = True, no_pm=True)
    async def df(self, ctx, interval:float, *, role):
	
        roleObj = discord.utils.find(lambda r: r.name == role, ctx.message.server.roles)
        if not roleObj:
            await self.bot.say("{} is not a valid role".format(role))
            return
        if interval < 120:
            interval = 120
        while True:
            colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            await self.bot.edit_role(ctx.message.server, roleObj, colour=discord.Colour(value=colour))
            await asyncio.sleep(interval)
	
	
	
def setup(bot):
    n = rainbow(bot)
    bot.add_cog(n)
