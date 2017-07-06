import discord
from discord.ext import commands

class Spam:
	"""Spam :D"""
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command()
	async def spam(self, ctx, user: discord.Member, spam_text: str, number: int):
		"""Spam The User hehe"""
		if spam_text == None:
			await self.bot.say('Wait What Dude Want To Spam Sombody Nothing Wew')
			return
		for i in range(number):
			await self.bot.send_message(user, spamtext)
			
def setup(bot):
	bot.add_cog(Spam(bot))
