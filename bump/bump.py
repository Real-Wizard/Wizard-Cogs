import discord
import asyncio
import sys
import traceback
import os
from discord.ext import commands

class bump:
    """Bump!"""

    def __init__(self, bot):
        self.bot = bot
    @commands.cooldown(1, 1500, type=commands.BucketType.server)
    @commands.command(pass_context=True)
    async def bump(self, ctx):
        """Bump your server!"""
        inv = await self.bot.create_invite(ctx.message.server)
        server = ctx.message.server
        count = 1
        channel = self.bot.get_channel("CHANNEL ID HERE")
        em = discord.Embed(title= "{}".format(server.name), color=0xFFFFFF, description="""
**Server Information**
:black_small_square: Server Owner : {}
:black_small_square: Member Count : {}
""".format(server.owner, server.member_count)) #0x0BFCF2 is the color code
        em.add_field(name='**Description**', value="""

:black_small_square: {}""".format(server.default_channel.topic))
        em.add_field(name='**Server Invite**', value="""

:black_small_square: {}""".format(inv))
        em.set_thumbnail(url=server.icon_url) #Or insert actual URL
        await self.bot.send_message(channel, embed=em)
        server = ctx.message.server
        des = server.default_channel.topic
        members = server.member_count
        inv = await self.bot.create_invite(ctx.message.server)
        message = "Server: {0} \n Description: {1} \n Users: {2} \n  Invite: {3}".format(server, des, members, inv)
        self.bot.send_message(channel, embed=em)
        end = discord.Embed(title="Your Server Was Succesfly Bumped")
        await self.bot.say(embed=end)

    @commands.command(pass_context=True, name="bumpcredits")
    async def __credits(self, ctx):
        """The Guy Who Made The Bump Seystem"""
        cr = discord.Embed(title="Creator", description="The Guy Who Made This Was MasterKnight#1375\n ID is 223754830747926528", color=0xFFFFFF)
        await self.bot.say(embed=cr)

    
def setup(bot):
    bot.add_cog(bump(bot))
