import discord
from discord.ext import commands
import subprocess
import sys

class Speedtest:

    def __init__(self,bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def speedtest(self):
        """SPEEEEEEEEED"""  
        await self.bot.say("SPEED TESTING...") 
        x = subprocess.check_output("speedtest-cli --secure --simple", shell=True).decode()
        #.split("\r\n")[9]
        await self.bot.say(x)

def setup(bot):
    n = Speedtest(bot)
    bot.add_cog(n)