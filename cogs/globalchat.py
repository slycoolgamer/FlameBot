import asyncio
import guilded
from guilded.ext import commands
import random
import os
import requests
import json

class globalchat(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        with open('DATABASE/channels.json') as f:
            channels = json.load(f)
        if message.channel.id in channels:
            for channel_id in channels:
                if channel_id != message.channel.id:
                    channel = self.bot.get_channel(channel_id)
                    await channel.send(f'{message.author} sent a message in {message.guild}: {message.content}')

def setup(bot):
    bot.add_cog(globalchat(bot))