import asyncio
import guilded
from guilded.ext import commands
import random
import os
import requests

class welcomer(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
           
def setup(bot):
    bot.add_cog(welcomer(bot))