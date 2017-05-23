import aiohttp
import discord
import json
from discord.ext import commands

class jokes:
	"""Jokes"""
	def __init__(self, bot):
		self.bot = bot

	@commands.command(pass_context=True)
	async def pun(self, ctx):
		"""Sends You a Random Pun"""
		pun_url = 'http://www.punoftheday.com/cgi-bin/arandompun.pl'
		async with aiohttp.ClientSession() as session:
			async with session.get(pun_url) as data:
				pun_req = await data.text()
				pun_text = pun_req.split('&quot;')[1]
		embed = discord.Embed(color=0x1abc9c)
		embed.add_field(name='😒 Have A Pun', value='```\n' + pun_text + '\n```')
		await self.bot.say(embed=embed)
		
	@commands.command(pass_context=True)
	async def yomomma(self, ctx):
		"""Sends You a Random Yo Momma Joke"""
		resource = 'http://api.yomomma.info/'
		async with aiohttp.ClientSession() as session:
			async with session.get(resource) as data:
				data = await data.read()
				data = json.loads(data)
		joke = data['joke']
		if not joke.endswith('.'):
				joke += '.'
		embed = discord.Embed(color=0x1abc9c)
		embed.add_field(name='😂 A Yo Momma Joke', value='```\n' + joke + '\n```')
		await self.bot.say(embed=embed)


	@commands.command(pass_context=True)
	async def joke(ctx, self):
		"""Sends You a random Joke"""
		joke_url = 'http://api.icndb.com/jokes/random'
		async with aiohttp.get("http://api.icndb.com/jokes/random/") as response:
			result = await response.json()
		joke_text = result["value"]["joke"]
		embed = discord.Embed(color=0x1abc9c)
		embed.add_field(name='😆 Have A Random Joke', value='\n```' + joke_text + '\n```')
		await self.bot.say(embed=embed)

def setup(bot):
	bot.add_cog(jokes(bot))



