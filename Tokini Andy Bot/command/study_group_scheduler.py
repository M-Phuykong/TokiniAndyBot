
import discord
from discord.ext import commands, tasks
import pytz
import datetime

STUDY_GROUP_VOICE_CHANNEL_ID = 973585117907943525

class StudyGroupScheduler(commands.Cog):

    def __init__(self, bot) -> None:
        self.bot = bot

        self.create_study_group.start()

    def cog_unload(self):
        self.create_study_group.cancel()

    @tasks.loop(hours=24)
    async def create_study_group(self):
        """Create a study group every 60 seconds"""

        def next_weekday(d, weekday):
            days_ahead = weekday - d.weekday()
            if days_ahead <= 0: # Target day already happened this week
                days_ahead += 7
            return d + datetime.timedelta(days_ahead)

        open_study_group_channel = self.bot.get_channel(964010823863369748)
        server = self.bot.guilds[0]
        study_group_role = server.get_role(974205236250021919)

        cst_time = datetime.datetime.now(pytz.timezone('America/Chicago'))
        next_wednesday_date = next_weekday(cst_time.date(), 2)
        time_list = [datetime.datetime.strptime(f"{next_wednesday_date} 6:00:00 AM", '%Y-%m-%d %I:%M:%S %p'),
                     datetime.datetime.strptime(f"{next_wednesday_date} 1:00:00 PM", '%Y-%m-%d %I:%M:%S %p'),
                     datetime.datetime.strptime(f"{next_wednesday_date} 8:00:00 PM", '%Y-%m-%d %I:%M:%S %p'),]

        # Check if wednesday
        if cst_time.weekday() == 3:
            events  = await server.fetch_scheduled_events()

            if not events:
                for time in time_list:
                    await server.create_scheduled_event(
                        name = "Study Group",
                        description = "Weekly Study Group",
                        channel = self.bot.get_channel(STUDY_GROUP_VOICE_CHANNEL_ID),
                        start_time = pytz.timezone('America/Chicago').localize(time),
                        entity_type = discord.EntityType.voice)
                await open_study_group_channel.send(f"Hey {study_group_role.mention}! Next week study group schedule is up!")

    @create_study_group.before_loop
    async def before_create_study_group(self):
        """Wait until bot is ready before creating study group"""

        await self.bot.wait_until_ready()

async def setup(bot):
    await bot.add_cog(StudyGroupScheduler(bot))