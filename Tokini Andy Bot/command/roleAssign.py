from discord import RawReactionActionEvent
from discord.ext import commands
import discord
import strings

class roleAssign(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="Role")
    @commands.has_role(strings.getString("adminRoleID"))
    async def start(self, ctx):
        embed = discord.Embed(title="Which Textbook Are You Using Currently?", 
        colour = discord.Colour.from_rgb(219, 68, 68),
        description = "\nGenki 1 : :orange_book: \n\n Genki 2 : :green_book: \n\n Quartet 1 : :closed_book: \n\n Quartet 2 : :blue_book: \n\n Other : :books:",
        )
        message = await ctx.send(embed=embed)
        emojis = strings.getString("textbookEmoji")
        for emoji in emojis:
            await message.add_reaction(emojis[emoji])
        
        
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload: RawReactionActionEvent) :
        role = ""
        if payload.message_id == strings.getString("roleMessageID"):
            match payload.emoji.name:
                case "this":
                    role = discord.utils.get(payload.member.guild.roles ,name = "Newbies") 
                case "teehee":
                    role = discord.utils.get(payload.member.guild.roles ,name = "Inter") 
                case "S_GG":
                    role = discord.utils.get(payload.member.guild.roles ,name = "Advance")
        else:
            return 

        await payload.member.add_roles(role)

    

def setup(bot):
    bot.add_cog(roleAssign(bot))