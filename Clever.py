import discord
import asyncio
from discord.ext import commands
from cleverwrap import CleverWrap
cw = CleverWrap('CCCrw8x-1eic8qi3Q-mrPc1Sutw')
class clever:
	def __init__(self, client):
		self.client = client
    
async def clever(message):
    param = message.content[2:]
    if len(param) > 2:
        
        await message.channel.send(cw.say(param))
    else:
        await message.channel.send('use !m <message>')

def setup(client):
	client.add_cog(clever(client))
