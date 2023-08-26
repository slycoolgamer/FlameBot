import asyncio
import guilded
from guilded.ext import commands
import random
import os
import requests

class fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='say',description='Make the bot say something: +say sentence')
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def say(self, ctx, *, sentence):
        await ctx.send(sentence)
        
    @commands.command(name='compliment',description='Compliment a user: +complement user')
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def compliment(self, ctx, *, user):
        response = requests.get('https://complimentr.com/api')
        if response.status_code == 200:
            data = response.json()
            c = data['compliment']
            embed = guilded.Embed(title=f'Random compliment to {user}', description=f'{user} {c}')
            embed.color = 0xff6600 # dark blue color
            embed.set_footer(text='Flame - guilded.gg/Flame-Bot')
            await ctx.send(embed=embed)
        else:
            await ctx.send('Sorry, something went wrong with the API.')
    
    @commands.command(name='catfact',description='Send a random cat fact: +catfact')
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def catfact(self, ctx):
        response = requests.get('https://catfact.ninja/fact')
        if response.status_code == 200:
            data = response.json()
            fact = data['fact']
            embed = guilded.Embed(title='Random Cat Fact', description=f'{fact}')
            embed.color = 0xff6600 # dark blue color
            embed.set_footer(text='Flame - guilded.gg/Flame-Bot')
            await ctx.send(embed=embed)
        else:
            await ctx.send('Sorry, something went wrong with the API.')
            
    @commands.command(name='gay',description='says how gay someone is')
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def gay(self, ctx, *, user):
        gaylevel = random.randint(0, 150)
        chance = random.randint(0, 50)
        if chance == 0:
            d = f'{user} is ∞% Gay'
        else:
           d = f'{user} is {gaylevel}% Gay'     
        embed = guilded.Embed(title='Gay Level', description=d)
        embed.color = 0xff6600 # dark blue color
        embed.set_footer(text='Flame - guilded.gg/Flame-Bot')
        await ctx.send(embed=embed)
        
    @commands.command(name='rps',description='Play rock, paper, scissors with the bot')
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def rps(self, ctx, move):
        async def rpsembed(title, desc, color):
            embed = guilded.Embed(title=title, description=desc)
            embed.color = color # dark blue color
            embed.set_footer(text='Flame - guilded.gg/Flame-Bot')
            await ctx.send(embed=embed)
            
        moves = ['rock', 'paper', 'scissors']
        AiMove = random.choice(moves)
        
        async def wonrps():
            await rpsembed('You Won', f'You Picked {move}; Bot Picked {AiMove}', 0x00ff00)
        async def loserps():
            await rpsembed('You Lost', f'You Picked {move}; Bot Picked {AiMove}', 0xff0000)
        async def invalidrps():
            await rpsembed('Invalid move', f'{move} is not valid. Pick rock, paper, or scissors.', 0xff6600)
        
        if move not in moves:
            await invalidrps()
            return
        
        if move == AiMove:
            await rpsembed('It\'s a tie', f'You and the bot both picked {move}', 0xff6600)
            return
        
        if (move == 'rock' and AiMove == 'scissors') or (move == 'paper' and AiMove == 'rock') or (move == 'scissors' and AiMove == 'paper'):
            await wonrps()
        else:
            await loserps()

    
            
def setup(bot):
    bot.add_cog(fun(bot))