import discord
from discord.ext import commands

class Spam:
	"""Spam :D"""
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command()
	async def spam(self, ctx, user: discord.Member, spamtext, number: int):
		"""Spam The User hehe"""
		for i in range(number):
			await self.bot.send_message(user, spamtext)
			
def setup(bot):
	bot.add_cog(Spam(bot))
