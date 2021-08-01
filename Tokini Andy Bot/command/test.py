import discord
from discord.ext import commands

import strings 


class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        

    @commands.command(name="test")
    async def test(self, ctx):
        emoji = await ctx.guild.fetch_emoji(868919439708520550)
        embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
        embedVar.add_field(name="Field1", value="hi", inline=False)
        embedVar.add_field(name="Field2", value= strings.getString("BannerGreetingMessage"), inline=False)
        await ctx.send(embed = embedVar) 
        


def setup(bot):
    bot.add_cog(Test(bot))