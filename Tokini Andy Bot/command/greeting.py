
import discord
import os
from discord import message
from discord import embeds
from discord.ext import commands
from PIL import Image, ImageOps
from io import BytesIO



class Test(commands.Cog):
    def _init_(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = member.guild.get_channel(780374076434808855)  # 'general' channel id

        image = Image.open(os.path.join(os.getcwd(),'Image\greetingcard.png'))
        mask  = Image.open(os.path.join(os.getcwd(),'Image\mask.png')).convert("L")

        asset = member.avatar_url_as(size = 128)
        data = BytesIO(await asset.read())
        pfp = Image.open(data)
        pfp = ImageOps.fit(pfp, mask.size, centering=(0.5, 0.5))
        pfp.putalpha(mask)

        image.paste(pfp, (22,19))
        image.save("profile.jpg")

        await channel.send(file = discord.File("profile.jpg"))
        await channel.send(f'Hi {member.name}, welcome to my Discord server!')



def setup(bot):
    bot.add_cog(Test(bot))