from discord.ext import commands
from discord.message import Message
from discord.threads import Thread

JP_QUESTION_CHANNEL_ID = 1019707862693457940

JP_MESSAGE = """
Thanks for posting on <#{channel_id}>! 
It usually takes some time for someone to get back to you. 
In the mean time:
・Make sure you've searched jisho.org
・Do a search on google. Ex: これ vs それ
・Check <#746332929361182801> to see if there might be an answer to your question.

Please let us know if you've already found your answer by adding the ANSWERED tag.
"""

class JPQuestionReply(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: Message) -> None:

        author_id = [m.author.id async for m in message.channel.history()]
        
        if message.author.id == self.bot.user.id:
            return

        if self.bot.user.id in author_id:
            return

        if type(message.channel) is Thread:
            if message.channel.parent.name == "japanese-questions":
                
                await message.channel.send(JP_MESSAGE
                                .format(channel_id = JP_QUESTION_CHANNEL_ID))

async def setup(bot):
    await bot.add_cog(JPQuestionReply(bot))