import json
import requests

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

API_URL = "https://api-inference.huggingface.co/models/facebook/roberta-hate-speech-dynabench-r4-target"
headers = {"Authorization": "Bearer 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"}

class TokiniAndyBot(commands.Bot):

	def __init__(self) -> None:
		super().__init__(
				PREFIX,
				description = "Bot for the TokiniAndy Discord Group",
				activity = WATCHING_ACTIVITY,
				intents = Intents.all(),
				allowed_mentions=discord.AllowedMentions.all(), # Everyone/Users/Roles/Replied_User
				case_insensitive=True,
				strip_after_prefix=True)

		# Uses the Cog from Discord API
		# Git Example [https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be]
		# Get command
		self.initial_extensions = [
			'command.test',
			'command.greeting',
			'command.reply_to_message',
			'command.study_group_scheduler',]

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


	async def query(self, payload):
		response = requests.post(API_URL, headers=headers, json=payload)
		return response.json()

	async def on_message(self, message: Message, /) -> None:

		# output = await self.query({
		# 	"inputs": message.content,
		# 	"wait_for_model": True
		# })
		# if (output[0][0]['label'] == "hate" and output[0][0]['score']>= 0.85) \
		# 	or (output[0][1]['label'] == "hate" and output[0][1]['score'] >= 0.85):
		# 	return await message.delete()

		return await super().on_message(message)


bot = TokiniAndyBot()
bot.run(TOKEN)