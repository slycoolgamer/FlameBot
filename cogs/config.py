import asyncio
import guilded
from guilded.ext import commands
import random
import os
import requests
import json

class config(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file_path = "DATABASE/prefixes.json"
        self.prefix_data = {}
        
        if os.path.exists(self.file_path):
            with open(self.file_path) as f:
                self.prefix_data = json.load(f)
                
        
    def save_prefix_data(self):
        with open(self.file_path, "w") as f:
            json.dump(self.prefix_data, f)
            
      
           
    @commands.command()
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def prefix(self, ctx, *, prefix=None):
        # This command allows the user to change the bot's prefix for their server
        if prefix is None:
            # If no prefix is given, show the current prefix
            current_prefix = self.prefix_data.get(str(ctx.guild.id), "+")
            await ctx.send(f"The current prefix is {current_prefix}")
        else:
            # If a prefix is given, update the prefix data and save it to the file
            self.prefix_data[str(ctx.guild.id)] = prefix
            self.save_prefix_data()
            await ctx.send(f"The prefix has been changed to {prefix}")
           
def setup(bot):
    bot.add_cog(config(bot))