# imports
import guilded
from guilded.ext import commands
import random
import os
import requests
from dotenv import load_dotenv
load_dotenv()
import os
import pytube

TOKEN = os.getenv('TOKEN')

# bot configuration
bot = commands.Bot(command_prefix='+', owner_id='ArgBlPL4')
bot.remove_command('help')


def check_cog_loaded(cog_name):
    yes = cog_name in bot.cogs
    message = f'{cog_name} loaded {yes}'
    print(message)
    
# load all commands cogs
bot.load_extension('cogs.calculator')
check_cog_loaded('calculator')
bot.load_extension('cogs.fun')
check_cog_loaded('fun')
bot.load_extension('cogs.info')
check_cog_loaded('info')
bot.load_extension('cogs.config')
check_cog_loaded('config')
bot.load_extension('cogs.economy')
check_cog_loaded('economy')


# what to do on start up
@bot.event
async def on_ready():
    print('Ready')
    try:
        emoteid = 273245
        content = '+help'
        botuserid = 'mLLkODwm'
        token = TOKEN

        import requests; from requests.structures import CaseInsensitiveDict
        url = f"https://www.guilded.gg/api/v1/users/{botuserid}/status"
        headers = CaseInsensitiveDict()
        headers["Authorization"] = f"Bearer {token}"
        headers["Accept"] = "application/json"
        headers["Content-type"] = "application/json"

        data = {"content": content, "emoteId": emoteid}

        resp = requests.put(url, headers=headers, json=data)

    except Exception as e:
        import traceback
        print(''.join(traceback.format_exception(e, e, e.__traceback__)))
        

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
        # Get the remaining cooldown time in seconds
        cooldown = error.retry_after
        # Format the time as minutes and seconds
        minutes, seconds = divmod(cooldown, 60)
        # Send a message to the user with the remaining time
        await ctx.send(f"You are on cooldown! Please wait {minutes:.0f} minutes and {seconds:.0f} seconds before trying again.")
    elif isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('You are missing a required argument.')
    elif isinstance(error, commands.BadArgument):
        await ctx.send('You have provided an invalid argument.')


# run bot                
bot.run(TOKEN)