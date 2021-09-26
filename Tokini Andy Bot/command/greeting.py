
import discord
import os

from discord import guild
from discord.ext.commands.errors import DisabledCommand
import strings
from discord.ext import commands
from PIL import Image, ImageOps, ImageDraw, ImageFont
from io import BytesIO

from discord import Guild



class Greeting(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.font = ImageFont.truetype('Font/DENGB.TTF',size=73)
		self.smallfont = ImageFont.truetype('Font/STKAITI.TTF',size=70)

		
	@commands.Cog.listener()
	async def on_member_join(self, member):
		channel = member.guild.system_channel
		
		card_img = Image.open(os.path.join(os.getcwd(),'Image/greetingcard.png')).convert("RGB")
		mask  = Image.open(os.path.join(os.getcwd(),'Image/mask.png')).convert("L")
		mask = mask.resize((300,300))

		#Get User's profile and then resize it to fit mask
		asset = member.avatar_url
		data = BytesIO(await asset.read())
		pfp = Image.open(data).convert("RGB")
		pfp = ImageOps.fit(pfp, mask.size, centering=(0.5, 0.5))

		card_img.paste(pfp, (600,30), mask)

		#Draw text
		im_draw = ImageDraw.Draw(card_img)
		im_draw.text((card_img.width/2,400),member.name,font = self.font,fill=(255,255,255,255), anchor="ms")
		im_draw.text((375,650),strings.getString("bannerGreetingMessage"),font=self.smallfont,fill=(255,255,255,255))

		card_img.save("greeting.png")
		await channel.send(file = discord.File("greeting.png"))
		await channel.send(f'Welcome {member.mention}!')

		try:
			os.remove("greeting.png")
		except Exception as e:
			print(f"Error: {e}")

	@commands.Cog.listener()
	async def on_member_update(self, before, after):
		if before.pending != after.pending:
			role = discord.utils.get(before.guild.roles, name = strings.getString("startRole") )
			await after.add_roles(role)

def setup(bot):
	bot.add_cog(Greeting(bot))