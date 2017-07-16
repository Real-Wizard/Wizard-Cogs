import discord
from discord.ext import commands
import asyncio
import re as reg

def serv():
	def predicate(ctx):
		return ctx.message.server.id == '263573949152100352' or ctx.message.server.id == '288804504189534208' # heist or cult
	return commands.check(predicate)

class HServ:
	def __init__(self, bot):
		self.bot = bot
		
		self.winners_worth = 2 # calculations, how much winners are worth
		self.losers_worth = 1 # calculations, how much losers are worth

	def calculator(self, total_players: int, total_winners: int , winnings_per: int):
		total_losers = total_players-total_winners
		total_winnings = int(total_winners)*int(winnings_per)
		
		avg_winning = total_winnings / ((self.winners_worth*total_winners)+(self.losers_worth*total_losers))
		winners_win = self.winners_worth * avg_winning
		losers_win = self.losers_worth * int(avg_winning)
		winners_pay = winnings_per - int(winners_win)
		return winners_pay, losers_win
	
	@commands.command(pass_context=True)
	@serv()
	async def calculate(self, ctx, total_players: int, total_winners: int, winnings_per: int):
		"""Calculates payouts"""
		total_losers = total_players-total_winners
		total_winnings = int(total_winners)*int(winnings_per)
		
		avg_winning = total_winnings / ((self.winners_worth*total_winners)+(self.losers_worth*total_losers))
		winners_win = self.winners_worth * avg_winning
		losers_win = self.losers_worth * int(avg_winning)
		winners_pay = winnings_per - int(winners_win)
		await self.bot.say('```http\nEach winner should pay {} to the splitter.\nThe splitter should pay {} to each loser.```'.format(winners_pay, losers_win))

	@commands.command(pass_context=True)
	@serv()
	async def calc(self, ctx):
		"""Calculates payouts"""
		def check(msg):
			try:
				int(msg.content)
			except:
				return False
			return True
		
		await self.bot.say('```http\nTotal players in the heist:```')
		a = await self.bot.wait_for_message(author=ctx.message.author, check=check, channel=ctx.message.channel, timeout=10)
		if a is None:
			return
		await self.bot.say('```http\nTotal winners in the heist:```')
		b = await self.bot.wait_for_message(author=ctx.message.author, check=check, channel=ctx.message.channel, timeout=10)
		if b is None:
			return
		await self.bot.say('```http\nAmount of winnings per each winner:```')
		c = await self.bot.wait_for_message(author=ctx.message.author, check=check, channel=ctx.message.channel, timeout=10)
		if c is None:
			return
		
		total_players = int(a.content)
		total_winners = int(b.content)
		winnings_per = int(c.content)
		
		total_losers = total_players-total_winners
		total_winnings = int(total_winners)*int(winnings_per)
		
		avg_winning = total_winnings / ((self.winners_worth*total_winners)+(self.losers_worth*total_losers))
		winners_win = self.winners_worth * avg_winning
		losers_win = self.losers_worth * int(avg_winning)
		winners_pay = winnings_per - int(winners_win)
		await self.bot.say('```http\nEach winner should pay {} to the splitter.\nThe splitter should pay {} to each loser.```'.format(winners_pay, losers_win))

	@commands.command(pass_context=True)
	@serv()
	async def rcalc(self, ctx):
		"""Calculates payouts"""
		async def get_input(text, msg=None):
			res = ''
			nums = ['1\u20e3', '2\u20e3', '3\u20e3', '4\u20e3', '5\u20e3', '6\u20e3', '7\u20e3', '8\u20e3', '9\u20e3', '0\u20e3', '\u25c0', '\u23ed']
			
			if msg is None:
				m = await self.bot.say('```http\n{}: {}```'.format(text, res))
				for n in nums:
					await self.bot.add_reaction(m, n)
			else:
				m = await self.bot.edit_message(msg, new_content='```http\n{}: {}```'.format(text, res))
			
			q = 0
			while True:
				r = await self.bot.wait_for_reaction(emoji=nums, user=ctx.message.author, message=m, timeout=10)
				if r == None:
					await self.bot.say('Cancelling calculator for {}, you took too long.'.format(ctx.message.author.mention))
					await self.bot.delete_message(m)
					return -727, None
				await self.bot.remove_reaction(m, r.reaction.emoji, ctx.message.author)
				if r.reaction.emoji == '\u23ed':
					break
				if r.reaction.emoji == '\u25c0':
					res = res[:-1]
				else:
					res += r.reaction.emoji[0]
				await self.bot.edit_message(m, new_content='```http\n{}: {}```'.format(text, res))
			# await self.bot.delete_message(m)
			return int(res), m
		
		total_players, the_msg = await get_input('Total players in the heist')
		if total_players == -727:
			return

		total_winners, __ = await get_input('Total winners in the heist', the_msg)
		if total_winners == -727:
			return

		winnings_per, __ = await get_input('Amount of winnings per each winner', the_msg)
		if winnings_per == -727:
			return
		
		total_losers = total_players-total_winners
		total_winnings = int(total_winners)*int(winnings_per)
		
		avg_winning = total_winnings / ((self.winners_worth*total_winners)+(self.losers_worth*total_losers))
		winners_win = self.winners_worth * avg_winning
		losers_win = self.losers_worth * int(avg_winning)
		winners_pay = winnings_per - int(winners_win)
		
		await self.bot.clear_reactions(the_msg)
		t = '```http\nInput: crew of {}, {} winners, {} per each winner.\nEach winner should pay {} to the splitter.\nThe splitter should pay {} to each loser.```'
		await self.bot.edit_message(the_msg, new_content=t.format(total_players, total_winners, winnings_per, winners_pay, losers_win))
	
def setup(bot):
	bot.add_cog(HServ(bot))
