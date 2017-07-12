import discord
import asyncio
import sys
import traceback
import os
from discord.ext import commands
from .utils.dataIO import dataIO
from .utils import checks

class bump:
    """Bump!"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = dataIO.load_json("data/bump/settings.json")

    @commands.cooldown(1, 1500, type=commands.BucketType.server)
    @commands.command(pass_context=True)
    async def bump(self, ctx):
        """Bump your server!"""
        if "bumpchannel" not in self.settings or not self.settings["bumpchannel"]:
            await self.bot.say("No channel has been set for bump messages to go to!")
            return
        inv = await self.bot.create_invite(ctx.message.server)
        server = ctx.message.server
        count = 1
        channel = self.bot.get_channel(self.settings["bumpchannel"])
        if not channel:
            await self.bot.say("Something went wrong with getting the channel!")
            return
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
        end = discord.Embed(title="Your Server Was Succesfully Bumped")
        await self.bot.say(embed=end)
    
    @checks.is_owner()
    @commands.command(pass_context=True)
    async def bumpchannel(self, ctx, channel: discord.Channel=None):
        """Sets the channel to send bump messages to"""
        self.settings["bumpchannel"] = channel.id
        dataIO.save_json("data/bump/settings.json", self.settings)
        


def check_folder():
    if not os.path.isdir("data/bump"):
        os.mkdir("data/bump")

def check_file():
    if not dataIO.is_valid_json("data/bump/settings.json"):
        dataIO.save_json("data/bump/settings.json", {})
    
def setup(bot):
    check_folder()
    check_file()
    bot.add_cog(bump(bot))
