import asyncio
import guilded
from guilded.ext import commands
import random
import os
import requests

class verification(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
           
def setup(bot):
    bot.add_cog(verification(bot))