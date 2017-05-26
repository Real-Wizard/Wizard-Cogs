import discord
from discord.ext import commands

class Spam:
	"""Spam :D"""
	def __init__(self, bot):
		self.bot = bot
		
	@commands.command()
	async def spam(self, ctx, user: discord.Member, spamtext, number: int):
		"""Spam The User hehe"""	
