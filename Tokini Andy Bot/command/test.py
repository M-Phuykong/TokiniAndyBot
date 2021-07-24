import discord
from discord.ext import commands


class Test(commands.Cog):
    def _init_(self, bot):
        self.bot = bot

    @commands.command(name="test")
    async def test(self, ctx):
        await ctx.send("できました")


def setup(bot):
    bot.add_cog(Test(bot))