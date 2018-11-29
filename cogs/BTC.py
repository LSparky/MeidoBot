import json
import discord
from discord.ext import commands
import requests
urll = 'https://api.coindesk.com/v1/bpi/currentprice/BTC.json'
with open('token.json') as token_file:
	data = json.load(token_file)


class BTC:
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def BTC(self, ctx):
		data = requests.get(urll).json()
		cur = data['bpi']['USD']['rate']
		msg = str(cur)+" USD"
		await ctx.send(msg)

def setup(client):
	client.add_cog(BTC(client))

#{"time":{"updated":"Nov 29, 2018 18:44:00 UTC","updatedISO":"2018-11-29T18:44:00+00:00","updateduk":"Nov 29, 2018 at 18:44 GMT"},"disclaimer":"This data was produced from the CoinDesk Bitcoin Price Index (USD). Non-USD currency data converted using hourly conversion rate from openexchangerates.org","bpi":{"USD":{"code":"USD","rate":"4,305.4325","description":"United States Dollar","rate_float":4305.4325},"BTC":{"code":"BTC","rate":"1.0000","description":"Bitcoin","rate_float":1}}}
