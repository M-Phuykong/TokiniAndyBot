import json

import discord
from discord.ext import commands
from discord.flags import Intents

# Opening and extracting JSON file
with open('config.json', encoding="utf8") as f:
	config = json.load(f)

# Const
TOKEN = config['DISCORD_TOKEN']
PREFIX = config['PREFIX']

class TokiniAndyBot(commands.Bot):

	def __init__(self) -> None:
		super().__init__(
				PREFIX, 
				description = "A Simple Bot for the TokiniAndy Discord Group", 
				intents = Intents.all(),
				allowed_mentions=discord.AllowedMentions.all(), # Everyone/Users/Roles/Replied_User
				case_insensitive=True,
				strip_after_prefix=True)
		
		# Uses the Cog from Discord API
		# Git Example [https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be]
		# Get command
		self.initial_extensions = ['command.test', 'command.greeting']
		
	# this gets call before the bot logins 
	#
	async def setup_hook(self):
		for ext in self.initial_extensions:
			await self.load_extension(ext)
	
	async def close(self):
		await super.close()
		await self.session.close()

	async def on_ready(self):
		print(f'{self.user} has connected to Discord!')

	async def change_presence() -> None:
		return await super().change_presence(activity=discord.Activity(name="TokiniAndy", 
														type=discord.ActivityType.watching))

bot = TokiniAndyBot()
bot.run(TOKEN)