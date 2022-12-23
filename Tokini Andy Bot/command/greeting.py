
import os
import json
from io import BytesIO

import discord
from discord.ext import commands
from PIL import Image, ImageDraw, ImageFont, ImageOps

with open('config.json', encoding="utf8") as f:
	strings = json.load(f)

class Greeting(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.font = ImageFont.truetype('Font/DENGB.TTF',size=72)
		self.small_font = ImageFont.truetype('Font/STKAITI.TTF',size=70)

		
	@commands.Cog.listener()
	async def on_member_join(self, member):
		
		# get specify  channel
		#
		channel = member.guild.get_channel(int(strings["GREETING_CHANNEL"]))

		card_img = Image.open(os.path.join(os.getcwd(),'Image/greetingcard.png')).convert("RGB")
		mask  = Image.open(os.path.join(os.getcwd(),'Image/mask.png')).convert("L")
		mask = mask.resize((300,300))

		# Get User's profile and then resize it to fit mask
		asset = member.display_avatar
		data = BytesIO(await asset.read())
		pfp = Image.open(data).convert("RGB")
		pfp = ImageOps.fit(pfp, mask.size, centering=(0.5, 0.5))

		card_img.paste(pfp, (600,30), mask)

		# Draw text
		im_draw = ImageDraw.Draw(card_img)
		im_draw.text((card_img.width/2,400),member.name,font = self.font,fill=(255,255,255,255), anchor="ms")
		im_draw.text((375,650),strings["BANNER_GREETING_MESSAGE"],font=self.small_font,fill=(255,255,255,255))

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
			role = discord.utils.get(before.guild.roles, name = strings["START_ROLE"])
			await after.add_roles(role)

async def setup(bot):
	await bot.add_cog(Greeting(bot))