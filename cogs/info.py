import asyncio
import guilded
from guilded.ext import commands
import random
import os
import requests

class info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(name='help', description='get command help: +help')
    @commands.cooldown(1, 2, commands.BucketType.user)
    async def help(self, ctx, command=None):
        async def basicembed(T, D):
            embed = guilded.Embed(title=T, description=D)
            embed.color = 0xff6600 # dark blue color
            embed.set_footer(text='Flame - guilded.gg/Flame-Bot')
            await ctx.send(embed=embed)
        if command is None:
            embed = guilded.Embed(title='[🔥Help](https://www.guilded.gg/Flame-Bot)', description='Use `+help [command]` or `+help` for information about command usage')
            embed.color = 0xff6600 # dark blue color
            embed.add_field(name='Calculator', value='`+math: add, subtract, multiply, divide, randint, power`')
            embed.add_field(name='Fun', value='`+say, +catfact, +compliment, +gay, +rps`')
            embed.add_field(name='Economy', value='`+bal, +give, +work, +dep, +with, +lb, +rob, +allowrob`')
            embed.add_field(name='Help', value='`+help: optional command`')
            embed.set_footer(text='Flame - guilded.gg/Flame-Bot')
            await ctx.send(embed=embed)
        elif command == 'math':
            embed = guilded.Embed(title='+math command', description='This bot can perform math commands. here is how to use it')
            embed.color = 0xff6600 # dark blue color
            embed.add_field(name='+math add', value='`+math add [num1] [num2]`')
            embed.add_field(name='+math subtract', value='`+math subtract [num1] [num2]`')
            embed.add_field(name='+math multiply', value='`+math multiply [num1] [num2]`')
            embed.add_field(name='+math divide', value='`+math divide [num1] [num2]`')
            embed.add_field(name='+math randint', value='`+math randint [num1] [num2]`')
            embed.add_field(name='+math power', value='`+math power [num1] [num2]`')
            embed.set_footer(text='Flame - guilded.gg/Flame-Bot')
            await ctx.send(embed=embed)
        elif command == 'say':
            await basicembed('Make the bot say something:', '`+say [sentence]`')
        elif command == 'compliment':
            await basicembed('Compliment someone:', '`+compliment [user]`')
        elif command == 'catfact':
            await basicembed('Get random cat fact:', '`+catfact`')
        elif command == 'help':
            await basicembed('Get command help:', '`+help optional[command]`')
        elif command == 'gay':
            await basicembed('Get gay %:', '`+gay [user]`')
        elif command == 'rps':
            await basicembed('Play Rock, Paper, scissors:', '`+rps [move]`')
        elif command == 'bal':
            await basicembed('Check your money, or create a account:', '`+balance`')
        elif command == 'give':
            await basicembed('Give money to someone:', '`+give [user]`')
        elif command == 'work':
            await basicembed('Earn money:', '`+work`')
        elif command == 'dep':
            await basicembed('Put money in bank:', '`+dep [amount]`')
        elif command == 'withdrawal':
            await basicembed('take money out bank:', '`+with [amount]`')
        elif command == 'lb':
            await basicembed('see the leaderstats:', '`+lb optional[user]`')
        elif command == 'rob':
            await basicembed('rob someones pocket:', '`+rob [user]`')
        elif command == 'brob':
            await basicembed('rob someones bank this is now disabled:', '`+brob [user]`')
        elif command == 'allowrob':
            await basicembed('enable or disable rob:', '`+allowrob [true/false]`')
        else:
            embed = guilded.Embed(title='Invalid Command', description='This command does not exist go back to `+help` or do `+help math`')
            embed.color = 0xff6600 # dark blue color
            embed.set_footer(text='Flame - guilded.gg/Flame-Bot')
            await ctx.send(embed=embed)
   
def setup(bot):
    bot.add_cog(info(bot))