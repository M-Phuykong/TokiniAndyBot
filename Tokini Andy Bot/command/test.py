import discord
import json
from discord.ext import commands

with open('config.json', encoding="utf8") as f:
	strings = json.load(f)
        
class Test(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name="test")
    async def test(self, ctx):
        embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
        embedVar.add_field(name="Field1", value="hi", inline=False)
        embedVar.add_field(name="Field2", value= strings["BANNER_GREETING_MESSAGE"], inline=False)
        await ctx.send(embed = embedVar) 
        


async def setup(bot):
    await bot.add_cog(Test(bot))