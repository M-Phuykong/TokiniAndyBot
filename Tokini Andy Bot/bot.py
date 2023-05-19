import json

import discord
from discord.ext import commands
from discord.flags import Intents
from discord.message import Message

# Opening and extracting JSON file
with open('config.json', encoding="utf8") as f:
	config = json.load(f)

# Const
#
TOKEN = config['DISCORD_TOKEN']
PREFIX = config['PREFIX']

# general: 589645807284781088
# jp-questions: 1019707862693457940
# study-group: 964010823863369748
INCLUDE_CHANNEL = {589645807284781088, 1019707862693457940, 964010823863369748}

WATCHING_ACTIVITY = discord.Activity(name="Tokini Andy",
					url="https://www.youtube.com/watch?v=1ZKkPxncjLw",
					type=discord.ActivityType.watching)

class TokiniAndyBot(commands.Bot):

	def __init__(self) -> None:
		super().__init__(
				PREFIX,
				description = "A Simple Bot for the TokiniAndy Discord Group",
				activity = WATCHING_ACTIVITY,
				intents = Intents.all(),
				allowed_mentions=discord.AllowedMentions.all(), # Everyone/Users/Roles/Replied_User
				case_insensitive=True,
				strip_after_prefix=True)

		# Uses the Cog from Discord API
		# Git Example [https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be]
		# Get command
		self.initial_extensions = ['command.test', 'command.greeting', 'command.reply_to_message']

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

	async def on_message(self, message: Message, /) -> None:
		if message.channel.id in INCLUDE_CHANNEL:
			with open("log.txt", "a") as f:
				mes = message.content
				mes.strip().replace(",", " ")
				f.writelines(f"{mes}\n")
		return await super().on_message(message)



bot = TokiniAndyBot()
bot.run(TOKEN)