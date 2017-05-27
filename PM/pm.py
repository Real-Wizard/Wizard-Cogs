import discord
from discord.ext import commands

class PM:
	"""PM People Using The Bot"""
	def __init__(self, bot):
		self.bot = bot

		
    @commands.command()
    @checks.is_owner()
    async def pm(self, user_id: str, *, msg: str):
	"""Pm a User Using The Bot"""
        user = await self.bot.get_user_info(user_id)
        try:
            await self.bot.send_message(user, msg)
        except:
            await self.bot.say('Could not DM This User ( ' + user_id + ')')
        else:
            await self.bot.say('DM successfully sent.')
# IDEA FROM DANNY
def setup(bot):
	n = PM(bot)
	bot.add_cog(n)


