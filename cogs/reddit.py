import discord
import praw
import json
import datetime
from discord.ext import commands

with open('token.json') as token_file:
	data = json.load(token_file)
clientid = data['clientid']
client_secret = data['client_secret']

r = praw.Reddit(client_id=clientid, client_secret=client_secret, user_agent='Meido Bot')

class reddit:
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def meme(self, ctx):
		subreddit = r.subreddit('memes').random()
		if subreddit.url.endswith("jpg") or subreddit.url.endswith("png"):
			bigimg = subreddit.url
		else:
			bigimg = "https://i.imgur.com/bfj5S6z.png"

		embed = discord.Embed(title=subreddit.title, description="By: " +subreddit.author.name, url="https://www.reddit.com/r/memes/comments/{0}/".format(subreddit.id), colour=discord.Colour(0xfc471e), timestamp=datetime.datetime.now())
		embed.set_image(url=bigimg)
		embed.set_author(name="/r/memes", icon_url="https://images-eu.ssl-images-amazon.com/images/I/418PuxYS63L.png")
		embed.set_footer(text="Requested by " + ctx.message.author.name, icon_url=ctx.message.author.avatar_url)
		await ctx.send(embed=embed)
		fdfaff

def setup(client):
	client.add_cog(reddit(client))
