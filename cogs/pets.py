import asyncio
import guilded
from guilded.ext import commands
import random
import os
import requests
import json

bot = commands.Bot(command_prefix='!')

class pets(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file_path = "DATABASE/pets.json"
        self.pets_data = {}
        # Load the economy data from the file
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                self.pets_data = json.load(f)
        else:
            # Create an empty file if it does not exist
            with open(self.file_path, "w") as f:
                json.dump(self.pet_data, f)
                
    @commands.command(aliases=['pet'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def mypet(self, ctx):
        # Get the user's ID
        user_id = str(ctx.author.id)
        # Check if the user has an account in the pets data
        if user_id not in self.pets_data:
            # Create a new account
            self.pets_data[user_id] = {"petname": user_id, "Petlevel": 0, "AttackDMG": 5, "Health": 10}
            # Save the economy data to the file
            with open(self.file_path, "w") as f:
                json.dump(self.pet_data, f)
        # Get the user's pocket and bank balances from the economy data
        pet_name = self.pet_data[user_id]["petname"]
        pet_level = self.pet_data[user_id]["petlevel"]
        pet_attack = self.pet_data[user_id]["AttackDMG"]
        petmaxhealth = self.pet_data[user_id]["Health"]
        # Send a message to the user with their balances
        embed = guilded.Embed(title='Your Pet')
        embed.color = 0xff6600 # dark blue color
        embed.add_field(name='**{pet_name}**', value=f'`Level: **{pet_level}**`')
        embed.add_field(name='', value='')
        embed.add_field(name='Stats', value=f'`Attack: {pet_attack}\nMaxHealth: {petmaxhealth}`')
        embed.set_footer(text='Flame - guilded.gg/Flame-Bot')
        await ctx.send(embed=embed)
                
def setup(bot):
    bot.add_cog(pets(bot))
                