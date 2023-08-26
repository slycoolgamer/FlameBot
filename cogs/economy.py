import asyncio
import guilded
from guilded.ext import commands
import random
import os
import requests
import json


class economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.file_path = "DATABASE/economy.json"
        self.economy_data = {}
        # Load the economy data from the file
        if os.path.exists(self.file_path):
            with open(self.file_path, "r") as f:
                self.economy_data = json.load(f)
        else:
            # Create an empty file if it does not exist
            with open(self.file_path, "w") as f:
                json.dump(self.economy_data, f)
                
    @commands.command(aliases=['bal'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def balance(self, ctx):
        # Get the user's ID
        user_id = str(ctx.author.id)
        # Check if the user has an account in the economy data
        if user_id not in self.economy_data:
            # Create a new account with 0 coins as the default balance
            self.economy_data[user_id] = {"pocket": 0, "bank": 0, "Rob": 1, "workedtimes": 0, "banksize": 10000}
            # Save the economy data to the file
            with open(self.file_path, "w") as f:
                json.dump(self.economy_data, f)
        # Get the user's pocket and bank balances from the economy data
        pocket_balance = self.economy_data[user_id]["pocket"]
        bank_balance = self.economy_data[user_id]["bank"]
        # Send a message to the user with their balances
        embed = guilded.Embed(title='Your Balances')
        embed.color = 0xff6600 # dark blue color
        embed.add_field(name='💸', value=f'`Pocket: {pocket_balance}`')
        embed.add_field(name='', value='')
        embed.add_field(name='🏦', value=f'`Bank: {bank_balance}`')
        embed.set_footer(text='Flame - guilded.gg/Flame-Bot')
        await ctx.send(embed=embed)

    @commands.command()
    async def give(self, ctx, member: guilded.Member, amount: int):
        # Get the user's ID and the member's ID
        user_id = str(ctx.author.id)
        member_id = str(member.id)
        # Check if the user and the member have accounts in the economy data
        if user_id not in self.economy_data or member_id not in self.economy_data:
            # Send a message to the user that they or the member need to create an account first
            await ctx.send("You or the member you want to give to need to create an account first. Use the balance command to do so.")
            return
        # Check if the amount is positive and less than or equal to the user's balance
        if amount > 0 and amount <= self.economy_data[user_id]["pocket"]:
            # Subtract the amount from the user's balance and add it to the member's balance
            self.economy_data[user_id]["pocket"] -= amount
            self.economy_data[member_id]["pocket"] += amount
            # Save the economy data to the file
            with open(self.file_path, "w") as f:
                json.dump(self.economy_data, f)
            # Send a message to the user that they have given the amount to the member
            await ctx.send(f"You have given {amount} 🪙 to {member.name}.")
        else:
            # Send a message to the user that they have entered an invalid amount
            await ctx.send("You have entered an invalid amount. It must be positive and less than or equal to your balance.")
            
    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def work(self, ctx):
        # Get the user's ID
        user_id = str(ctx.author.id)
        # Check if the user has an account in the economy data
        if user_id not in self.economy_data:
            # Create a new account with 1000 coins as the default balance
            self.economy_data[user_id] = {"pocket": 0}
            # Save the economy data to the file
            with open(self.file_path, "w") as f:
                json.dump(self.economy_data, f)
    
        # Generate a random amount of coins between 100 and 500
        boost = self.economy_data[user_id]["Rob"] + 1 
        earnings = random.randint(100, 500 * boost)
        # Add the earnings to the user's balance
        self.economy_data[user_id]["pocket"] += earnings
        self.economy_data[user_id]["workedtimes"] += 1
        # Save the updated economy data to the file
        with open(self.file_path, "w") as f:
            json.dump(self.economy_data, f)
    
        # Send a message to the user with their earnings
        
        embed = guilded.Embed(title='Earned', description=f'`🪙{earnings} with {boost}x boost`')
        embed.color = 0xff6600 # dark blue color
        embed.set_footer(text='Flame - guilded.gg/Flame-Bot')
        await ctx.send(embed=embed)
     
    @commands.command(aliases=['deposit'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def dep(self, ctx, amount: int):
        # Get the user's ID
        user_id = str(ctx.author.id)
        # Check if the user has an account in the economy data
        if user_id not in self.economy_data:
            # Create a new account with 1000 coins as the default balance
            self.economy_data[user_id] = {"pocket": 0, "bank": 0}
            # Save the economy data to the file
            with open(self.file_path, "w") as f:
                json.dump(self.economy_data, f)
        # Check if the user has enough coins in their pocket to deposit
        if amount <= self.economy_data[user_id]["pocket"]:
            # Subtract the amount from the user's pocket and add it to their bank
            self.economy_data[user_id]["pocket"] -= amount
            self.economy_data[user_id]["bank"] += amount
            # Save the economy data to the file
            with open(self.file_path, "w") as f:
                json.dump(self.economy_data, f)
            # Send a message to the user confirming the deposit
            await ctx.send(f"You have deposited {amount} 🪙 into your bank.")
        else:
            # Send a message to the user indicating that they don't have enough coins in their pocket
            await ctx.send("You don't have enough coins in your pocket to deposit.")

    @commands.command(aliases=['with'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def withdrawal(self, ctx, amount: int):
        # Get the user's ID
        user_id = str(ctx.author.id)
        # Check if the user has an account in the economy data
        if user_id not in self.economy_data:
            # Create a new account with 1000 coins as the default balance
            self.economy_data[user_id] = {"pocket": 0, "bank": 0}
            # Save the economy data to the file
            with open(self.file_path, "w") as f:
                json.dump(self.economy_data, f)
        # Check if the user has enough coins in their bank to withdraw
        if amount <= self.economy_data[user_id]["bank"]:
            # Subtract the amount from the user's bank and add it to their pocket
            self.economy_data[user_id]["bank"] -= amount
            self.economy_data[user_id]["pocket"] += amount
            # Save the economy data to the file
            with open(self.file_path, "w") as f:
                json.dump(self.economy_data, f)
            # Send a message to the user confirming the withdrawal
            await ctx.send(f"You have withdrawn {amount} 🪙 from your bank.")
        else:
            # Send a message to the user indicating that they don't have enough coins in their bank
            await ctx.send("You don't have enough coins in your bank to withdraw.")
            
    @commands.command(aliases=['lb'])
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def leaderboard(self, ctx, *, username=None):
        # Sort the economy data by combined pocket and bank balances in descending order
        sorted_data = sorted(
            self.economy_data.items(),
            key=lambda x: x[1]["pocket"] + x[1]["bank"],
            reverse=True
    )

        if username:
            # Find the user's placement in the leaderboard
            user_placement = None
            for index, (user_id, _) in enumerate(sorted_data, start=1):
                user = ctx.guild.get_member(user_id)
                if user and user.display_name.lower() == username.lower():
                    user_placement = index
                    break

            if user_placement:
                await ctx.send(f"{username} is ranked #{user_placement} on the leaderboard!")
            else:
                await ctx.send(f"{username} is not found on the leaderboard.")
        else:
            # Create the leaderboard embed
            embed = guilded.Embed(title='Leaderboard')
            embed.color = 0xff6600  # dark blue color
        
            # Add the top 5 users to the leaderboard embed
            for index, (user_id, balances) in enumerate(sorted_data[:5], start=1):
                user = ctx.guild.get_member(user_id)
                if user:
                    pocket_balance = balances["pocket"]
                    bank_balance = balances["bank"]
                    total_balance = pocket_balance + bank_balance
                    embed.add_field(
                        name=f'{index}. {user.display_name}',
                        value=f'💸 Pocket: {pocket_balance}\n🏦 Bank: {bank_balance}\nTotal: {total_balance}',
                        inline=False
                )
        
            embed.set_footer(text='Flame - guilded.gg/Flame-Bot')
            await ctx.send(embed=embed)
    
    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def rob(self, ctx, member: guilded.Member):
        # Get the user's ID and the member's ID
        user_id = str(ctx.author.id)
        member_id = str(member.id)
        # Check if the user and the member have accounts in the economy data
        if user_id not in self.economy_data or member_id not in self.economy_data:
            # Send a message to the user that they or the member need to create an account first
            await ctx.send("You or the member you want to give to need to create an account first. Use the balance command to do so.")
            return
        else:
            if self.economy_data[member_id]["Rob"] == 1:
                pick = random.randint(0, 4)
                if pick == 4:
                    amount = random.randint(0, self.economy_data[member_id]["pocket"] // 4)
                    # Subtract the amount from the user's balance and add it to the member's balance
                    self.economy_data[user_id]["pocket"] -= amount
                    self.economy_data[member_id]["pocket"] += amount
                    # Save the economy data to the file
                    with open(self.file_path, "w") as f:
                        json.dump(self.economy_data, f)
                # Send a message to the user that they have given the amount to the member
                    await ctx.send(f"You have been fined {amount} 🪙 by {member.name}.")
                else:
                    amount = random.randint(0, self.economy_data[member_id]["pocket"] // 8)
                    # Subtract the amount from the user's balance and add it to the member's balance
                    if amount < self.economy_data[user_id]["Pocket"]:
                        self.economy_data[user_id]["pocket"] += amount
                        self.economy_data[member_id]["pocket"] -= amount
                        # Save the economy data to the file
                        with open(self.file_path, "w") as f:
                            json.dump(self.economy_data, f)
                        # Send a message to the user that they have given the amount to the member
                        await ctx.send(f"You have robbed {amount} 🪙 from {member.name}.")
                    if amount > self.economy_data[user_id]["Pocket"]:
                        await ctx.send(f"You have failed {member.name} has chosen to not fine.")
            elif self.economy_data[member_id]["Rob"] == 0:
                await ctx.send(f"{member.name} has rob disabled.")
                              
    @commands.command(aliases=['ar'])
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def allowrob(self, ctx, set):
        # Get the user's ID and the member's ID
        user_id = str(ctx.author.id)
        if user_id not in self.economy_data:
            # Send a message to the user that they or the member need to create an account first
            await ctx.send("You or the member you want to give to need to create an account first. Use the balance command to do so.")
            return
        else:
            if set == 'true':
                self.economy_data[user_id]["Rob"] = 1
                with open(self.file_path, "w") as f:
                        json.dump(self.economy_data, f)
                await ctx.send("You Set Allow rob to true")
            elif set == 'false':
                self.economy_data[user_id]["Rob"] = 0
                with open(self.file_path, "w") as f:
                        json.dump(self.economy_data, f)
                await ctx.send("You Set Allow rob to false")
            else:
                await ctx.send("pick argument true, false")
                
    
    
                

                
def setup(bot):
    bot.add_cog(economy(bot))