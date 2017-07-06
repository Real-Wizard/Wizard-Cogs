from discord.ext import commands
import asyncio

class Nik:
    """lul"""
    def __init__(self, bot):
    	self.bot = bot

    @commands.command(pass_context=True)
    async def nik(self, ctx, times : int=None):
        """\U00000028 \U00000361\U000000b0 \U0000035c\U00000296 \U00000361\U000000b0\U00000029"""
        if times == None:
            times = 1
        elif times > 50:
            times = 50
        delay = ((times * 1.00 / 10) + 1.0)
        counter = 0
        while counter < times:
            await self.bot.edit_message(ctx.message, 'n')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, 'ni')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, 'nik')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, 'nikh')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, 'nikhi')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, 'nikhil')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, 'nikhil <')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, 'nikhil <6')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, 'nikhil <69')
            await asyncio.sleep(delay)
            counter = counter + 1

def setup(bot):
	bot.add_cog(Nik(bot))
