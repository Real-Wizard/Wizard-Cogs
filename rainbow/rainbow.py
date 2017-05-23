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
	
    @checks.admin_or_permissions(manage_roles=True)
    @commands.command(pass_context = True, no_pm=True)
    async def rainbow(self, ctx, *, role: discord.Role):
        
        while True:
            colour = ''.join([choice('0123456789ABCDEF') for x in range(6)])
            colour = int(colour, 16)
            await self.bot.edit_role(ctx.message.server, role, colour=discord.Colour(value=colour))
            await asyncio.sleep(1.0)
	
def setup(bot):
    n = rainbow(bot)
    bot.add_cog(n)
