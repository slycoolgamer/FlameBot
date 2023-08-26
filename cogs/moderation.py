import asyncio
import guilded
from guilded.ext import commands
import random
import os
import requests

class moderation(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
            
        
        
#python
#permissions = bot.get_permissions_for(user, server)
#if permissions.has("manage_server"):
# do something
#else:
# do something else
#```

#This way, you can check for any permission that is available in the guilded.py library without relying on the has_permission attribute.
#```
               
def setup(bot):
    bot.add_cog(moderation(bot))
    
