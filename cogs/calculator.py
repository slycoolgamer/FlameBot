import asyncio
import guilded
from guilded.ext import commands
import random
import os
import requests
import math

class calculator(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
   
    @commands.command(name='math',description='Do math commands')
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def math(self, ctx, op, num1, num2):
        if op == 'add':
            calc = int(num1) + int(num2)
            embed = guilded.Embed(title='Addition Complete', description=f'The operation {num1} + {num2} = {str(calc)}')
            embed.color = 0xff6600 # dark blue color
            embed.set_footer(text='Flame - guilded.gg/Flame-Bot')
            await ctx.send(embed=embed)
        
        elif op == 'subtract':
            calc = int(num1) - int(num2)
            embed = guilded.Embed(title='Subtraction Complete', description=f'The operation {num1} - {num2} = {str(calc)}')
            embed.color = 0xff6600 # dark blue color
            embed.set_footer(text='Flame - guilded.gg/Flame-Bot')
            await ctx.send(embed=embed)
        elif op == 'multiply':
            calc = int(num1) * int(num2)
            embed = guilded.Embed(title='Multiplication Complete', description=f'The operation {num1} x {num2} = {str(calc)}')
            embed.color = 0xff6600 # dark blue color
            embed.set_footer(text='Flame - guilded.gg/Flame-Bot')
            await ctx.send(embed=embed)
        elif op == 'divide':
            calc = int(num1) / int(num2)
            embed = guilded.Embed(title='Division Complete', description=f'The operation {num1} ÷ {num2} = {str(calc)}')
            embed.color = 0xff6600 # dark blue color
            embed.set_footer(text='Flame - guilded.gg/Flame-Bot')
            await ctx.send(embed=embed)
        elif op == 'randint':
            number = random.randint(int(num1), int(num2))
            strnum = str(number)
            embed = guilded.Embed(title='Random Int Generated', description=f'The interger between {num1} and {num2} = {strnum}')
            embed.color = 0xff6600 # dark blue color
            embed.set_footer(text='Flame - guilded.gg/Flame-Bot')
            await ctx.send(embed=embed)
        elif op == 'power':
            number = math.pow(int(num1), int(num2))
            strnum = str(number)
            embed = guilded.Embed(title='Power Complete', description=f'Power {num1} by {num2} and got {strnum}')
            embed.color = 0xff6600 # dark blue color
            embed.set_footer(text='Flame - guilded.gg/Flame-Bot')
            await ctx.send(embed=embed)
        else:
            await ctx.send('invalid operation must be add sub mul div randint')

def setup(bot):
    bot.add_cog(calculator(bot))
