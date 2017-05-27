import discord
import datetime
from cogs.utils import checks
from discord.ext import commands

__spiced_up_by__ = "Young™#5484"

class Whisper:
    """PM People Using The Bot"""
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def whisper(self, ctx, user_id: str, *, msg: str):
        """Dm users."""
        user = await self.bot.get_user_info(user_id)
        try:
            e = discord.Embed(colour=discord.Colour.red())
            e.title = "You've recieved a message from a developer!"
            e.add_field(name="Developer:", value=ctx.message.author, inline=False)
            e.add_field(name="Time:", value=datetime.datetime.now().strftime("%A, %B %-d %Y at %-I:%M%p").replace("PM", "pm").replace("AM", "am"), inline=False)
            e.add_field(name="Message:", value=msg, inline=False)
            e.set_thumbnail(url=ctx.message.author.avatar_url)
            await self.bot.send_message(user, embed=e)
        except:
            await self.bot.say(':x: Failed to send message to user_id `{}`.'.format(user_id))
        else:
            await self.bot.say('Succesfully sent message to {}'.format(user_id))		

def setup(bot):
    n = Whisper(bot)
    bot.add_cog(n)


