import discord
from discord.ext import commands
import os
from .utils.dataIO import fileIO

default_settings = {"SERVER": {"DEFAULT": False}}

class ayy:
    """lmaoing"""

    def __init__(self, bot):
        self.bot = bot
        self.settings = fileIO("data/ayy/settings.json", "load")

    @commands.command(pass_context=True, no_pm=True)
    async def ayy(self, ctx):
        """Toggle lmaoing for this server"""
        server = ctx.message.server
        if server.id not in self.settings["SERVER"]:
            self.settings["SERVER"][
                server.id] = default_settings["SERVER"]["DEFAULT"]
        self.settings["SERVER"][
            server.id] = not self.settings["SERVER"][server.id]
        if self.settings["SERVER"][server.id]:
            await self.bot.say("I will now lmao to ayy.")
        else:
            await self.bot.say("I won't lmao anymore.")
        fileIO("data/ayy/settings.json", "save", self.settings)

    async def check_ayy(self, message):
        if "ayy" in message.content.split():
            if self.settings["SERVER"].get(server.id, False):
                await self.bot.say("Looks like lmaoing isn't enabled! Do `!ayy`v")
            else:
                await self.bot.send_message(message.channel, "lmao")

def check_folders():
    if not os.path.exists("data/ayy"):
        print("Creating ayy folder...")
        os.makedirs("data/ayy")


def check_files(bot):
    settings_path = "data/ayy/settings.json"

    if not os.path.isfile(settings_path):
        print("Creating default ayy settings.json...")
        fileIO(settings_path, "save", default_settings)

def setup(bot):
    check_folders()
    check_files(bot)
    n = ayy(bot)
    bot.add_listener(n.check_ayy, "on_message")
    bot.add_cog(n)