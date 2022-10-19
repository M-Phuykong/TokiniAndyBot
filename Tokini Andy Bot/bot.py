import json
from PIL.ImageFont import truetype

import discord
from discord.ext import commands
from discord.flags import Intents

# Opening and extracting JSON file
f = open('config.json')
config = json.load(f)
f.close()

# Const
TOKEN = config['DISCORD_TOKEN']
PREFIX = config['PREFIX']

# Set permission for bot(Changed after v1.5.0)
intent = Intents.default()
intent.members = True


bot = commands.Bot(
	command_prefix=PREFIX,
	intents=intent, 
	allowed_mentions=discord.AllowedMentions.all(), # Everyone/Users/Roles/Replied_User
	case_insensitive=True,
	strip_after_prefix=True
)

# Uses the Cog from Discord API
# Git Example [https://gist.github.com/EvieePy/d78c061a4798ae81be9825468fe146be]
# Get command
initial_commands = ['command.test',
					'command.greeting']

# Load command
if __name__ == '__main__':
	for command in initial_commands:
		bot.load_extension(command)


@bot.event
async def on_ready():
	print(f'{bot.user} has connected to Discord!')

	await bot.change_presence(activity=discord.Activity(name="TokiniAndy", 
														type=discord.ActivityType.watching,
																												
														))



try:
	bot.run(TOKEN)
except Exception as e:
	print(f"Error: {e}")
