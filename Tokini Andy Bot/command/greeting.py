
import discord
import os
import strings
from discord.ext import commands
from PIL import Image, ImageOps, ImageDraw, ImageFont
from io import BytesIO



class Greeting(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
		self.font = ImageFont.truetype("STKAITI.TTF", 28)
		self.smallfont = ImageFont.truetype("STKAITI.TTF", 20)

		
	@commands.Cog.listener()
	async def on_member_join(self, member):
		channel = member.guild.system_channel
		
		card_img = Image.open(os.path.join(os.getcwd(),'Image\greetingcard.png')).convert("RGB")
		mask  = Image.open(os.path.join(os.getcwd(),'Image\mask.png')).convert("L")

		#Get User's profile and then resize it to fit mask
		asset = member.avatar_url
		data = BytesIO(await asset.read())
		pfp = Image.open(data).convert("RGB")
		pfp = ImageOps.fit(pfp, mask.size, centering=(0.5, 0.5))

		card_img.paste(pfp, (20,19), mask)

		#Draw text
		im_draw = ImageDraw.Draw(card_img)
		im_draw.text((160,27),member.name, font= self.font,fill=(255,0,0,1))
		im_draw.text((160,100),strings.getString("BannerGreetingMessage"), font= self.smallfont,fill=(255,0,0,1))
	

		card_img.save("greeting.png")

		await channel.send(file = discord.File("greeting.png"))
		await channel.send(f'Hi {member.mention}, welcome to my Discord server!')

		try:
			os.remove("greeting.png")
		except Exception as e:
			print(f"Error: {e}")

def setup(bot):
	bot.add_cog(Greeting(bot))