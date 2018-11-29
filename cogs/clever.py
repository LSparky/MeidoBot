#script scuffed by bahka, fixed up by Sparky

import discord
import json
from discord.ext import commands
from cleverwrap import CleverWrap

with open('token.json') as token_file:
	data = json.load(token_file)
clevertoken = data['clevertoken']

cw = CleverWrap(clevertoken)

class clever:
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def cb(self, ctx, arg1):
		await ctx.send(cw.say(arg1))

	@cb.error
	async def cb_error(self, ctx, error):
		if isinstance(error, commands.MissingRequiredArgument):
			await ctx.send("Please enter a message with quotation marks around it!")

	@commands.command()
	async def cb_reset(self, ctx):
		cw.reset()
		await ctx.send("Reset conversation!")

def setup(client):
	client.add_cog(clever(client))
