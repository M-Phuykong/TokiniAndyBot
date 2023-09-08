from discord.ext import commands
from discord.message import Message
from discord.threads import Thread
from discord.channel import TextChannel

JP_QUESTION_CHANNEL_ID = 1019707862693457940
INTRODUCE_YOURSELF_CHANNEL_ID = 678941912329224202

JP_MESSAGE = """
Thanks for posting on <#{channel_id}>!
It usually takes some time for someone to get back to you.
In the mean time:
・Make sure you've searched jisho.org
・Do a search on google. Ex: これ vs それ
・Check <#746332929361182801> to see if there might be an answer to your question.

Please let us know if you've already found your answer by adding the ANSWERED tag.
"""

INTRODUCE_YOURSELF_REPLY = """
Hi {member_mention}, welcome to the Tokini Andy Discord server! Thank you for the post. Please make sure to check out <#746332929361182801> for study tips / tools. Also checkout the <#801325713088315433> for server tags. For questions please post in <#1019707862693457940> (please look at pinned comments for optimal guide. Good luck in your learning.
"""



class ReplyMessage(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot
        self.introduce_yourself_hashmap = set()

    @commands.Cog.listener()
    async def on_message(self, message: Message) -> None:


        author_id = set([m.author.id async for m in message.channel.history()])

        # exit if message is from bot
        #
        if message.author.bot:
            return

        if type(message.channel) is Thread:

            if message.channel.parent.name == "japanese-questions":

                # return if bot already replied
                #
                if self.bot.user.id in author_id:
                    return

                await message.channel.send(JP_MESSAGE
                                .format(channel_id = JP_QUESTION_CHANNEL_ID))

        if type(message.channel) is TextChannel:

            if message.author.id in self.introduce_yourself_hashmap:
                return

            if message.channel.id == INTRODUCE_YOURSELF_CHANNEL_ID:
                self.introduce_yourself_hashmap.add(message.author.id)
                await message.channel.send(INTRODUCE_YOURSELF_REPLY.format(member_mention = message.author.mention))


async def setup(bot):
    await bot.add_cog(ReplyMessage(bot))