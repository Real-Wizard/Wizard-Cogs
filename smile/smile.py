from discord.ext import commands
import asyncio

class Smile:
    """Smile."""
    def __init__(self, bot):
    	self.bot = bot

    @commands.command(pass_context=True)
    async def smile(self, ctx, times : int=None):
        """\U00000028 \U00000361\U000000b0 \U0000035c\U00000296 \U00000361\U000000b0\U00000029"""
        if times == None:
            times = 1
        elif times > 50:
            times = 50
        delay = ((times * 1.05 / 10) + 1.5)
        counter = 0
        while counter < times:
            await self.bot.edit_message(ctx.message, ':grinning:')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, ':smile:')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, ':grinning:')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, ':smile:')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, ':grinning:')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, ':smile:')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, ':grinning:')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, ':smile:')
            await asyncio.sleep(delay)
            await self.bot.edit_message(ctx.message, ':grinning:')
            await asyncio.sleep(delay)
            counter = counter + 1

def setup(bot):
	bot.add_cog(Smile(bot))
