import discord
from discord.ext import commands
import os

class ayy:
    """lmaoing"""

    def __init__(self, bot):
        self.bot = bot

    async def check_ayy(self, message):
        if "ayy" in message.content.split():
            await self.bot.send_message(message.channel, "lmao")

def setup(bot):
    n = ayy(bot)
    bot.add_listener(n.check_ayy, "on_message")
    bot.add_cog(n)